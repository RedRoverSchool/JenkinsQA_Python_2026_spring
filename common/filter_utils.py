from __future__ import annotations

import ast
import os
from collections import defaultdict, deque
from pathlib import Path

_CHANGED_FILES_ENV = "LIST_OF_CHANGED_FILES"
_CHANGED_FILES_SEPARATOR = ";"
_IGNORED_DIR_NAMES = {".git", ".idea", ".pytest_cache", "__pycache__", "venv", ".venv"}


def filter_items_by_changed_files(items):
    changed_files_raw = os.getenv(_CHANGED_FILES_ENV, "")
    if not changed_files_raw.strip():
        return items

    changed_entries = _parse_changed_entries(changed_files_raw)
    if not changed_entries:
        return items

    if any(not _is_python_file_path(entry) for entry in changed_entries):
        return items

    project_root = Path(__file__).resolve().parents[1]
    project_python_files = _collect_project_python_files(project_root)
    if not project_python_files:
        return items

    module_alias_map = _build_module_alias_map(project_python_files)
    dependency_graph = _build_dependency_graph(project_root, project_python_files, module_alias_map)
    reverse_graph = _build_reverse_dependency_graph(dependency_graph)

    changed_python_files = {
        _match_repo_file(changed_entry, project_python_files)
        for changed_entry in changed_entries
    }
    changed_python_files = {path for path in changed_python_files if path}

    if not changed_python_files:
        return items

    impacted_files = _collect_impacted_files(changed_python_files, reverse_graph)
    if any(Path(file_path).name == "conftest.py" for file_path in impacted_files):
        return items

    filtered_items = []
    for item in items:
        item_file = _resolve_item_python_file(item, project_python_files)
        if item_file is None or item_file in impacted_files:
            filtered_items.append(item)

    return filtered_items


def _parse_changed_entries(changed_files_raw: str) -> list[str]:
    entries = []
    for raw_entry in changed_files_raw.split(_CHANGED_FILES_SEPARATOR):
        normalized_entry = raw_entry.strip()
        if not normalized_entry:
            continue

        for path_part in normalized_entry.split("->"):
            cleaned_path = _clean_path_token(path_part)
            if cleaned_path:
                entries.append(cleaned_path)

    return entries


def _clean_path_token(path_token: str) -> str:
    cleaned = path_token.strip().strip("\"'")
    if not cleaned:
        return ""

    if "\t" in cleaned:
        status_and_path = cleaned.split("\t", 1)
        if len(status_and_path) == 2 and _looks_like_status_token(status_and_path[0]):
            cleaned = status_and_path[1].strip()

    space_split = cleaned.split(" ", 1)
    if len(space_split) == 2 and _looks_like_status_token(space_split[0]):
        cleaned = space_split[1].strip()

    return cleaned.replace("\\", "/")


def _looks_like_status_token(token: str) -> bool:
    normalized = token.strip().upper()
    if not normalized:
        return False
    if normalized in {"A", "M", "D", "R", "C", "T", "U"}:
        return True
    return normalized[0] in {"R", "C"} and normalized[1:].isdigit()


def _is_python_file_path(path_value: str) -> bool:
    return Path(path_value).suffix.lower() == ".py"


def _collect_project_python_files(project_root: Path) -> set[str]:
    python_files = set()
    for root, dirnames, filenames in os.walk(project_root):
        dirnames[:] = [dirname for dirname in dirnames if dirname not in _IGNORED_DIR_NAMES]
        for filename in filenames:
            if not filename.endswith(".py"):
                continue
            full_path = Path(root) / filename
            relative_path = full_path.relative_to(project_root).as_posix()
            python_files.add(relative_path)

    return python_files


def _build_module_alias_map(project_python_files: set[str]) -> dict[str, set[str]]:
    alias_map: dict[str, set[str]] = defaultdict(set)
    for file_path in project_python_files:
        module_parts = Path(file_path).with_suffix("").parts
        module_name = ".".join(module_parts)
        alias_map[module_name].add(file_path)
        alias_map[module_parts[-1]].add(file_path)

    return alias_map


def _build_dependency_graph(
    project_root: Path,
    project_python_files: set[str],
    module_alias_map: dict[str, set[str]],
) -> dict[str, set[str]]:
    graph = {file_path: set() for file_path in project_python_files}
    for file_path in project_python_files:
        source_path = project_root / file_path
        try:
            source = source_path.read_text(encoding="utf-8")
            tree = ast.parse(source)
        except (OSError, SyntaxError, UnicodeDecodeError):
            continue

        current_module = ".".join(Path(file_path).with_suffix("").parts)
        current_package = current_module.split(".")[:-1]

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    graph[file_path].update(module_alias_map.get(alias.name, ()))
            elif isinstance(node, ast.ImportFrom):
                base_module = _resolve_from_base_module(node.module, node.level, current_package)
                if base_module:
                    graph[file_path].update(module_alias_map.get(base_module, ()))

                for alias in node.names:
                    if alias.name == "*":
                        continue
                    import_target = f"{base_module}.{alias.name}" if base_module else alias.name
                    graph[file_path].update(module_alias_map.get(import_target, ()))

        graph[file_path].discard(file_path)

    return graph


def _resolve_from_base_module(module: str | None, level: int, current_package: list[str]) -> str:
    if level <= 0:
        return module or ""

    keep_count = max(len(current_package) - (level - 1), 0)
    prefix_parts = current_package[:keep_count]
    if module:
        prefix_parts.extend(module.split("."))

    return ".".join(part for part in prefix_parts if part)


def _build_reverse_dependency_graph(graph: dict[str, set[str]]) -> dict[str, set[str]]:
    reverse_graph: dict[str, set[str]] = defaultdict(set)
    for source_file, imported_files in graph.items():
        for imported_file in imported_files:
            reverse_graph[imported_file].add(source_file)

    return reverse_graph


def _collect_impacted_files(
    changed_files: set[str],
    reverse_graph: dict[str, set[str]],
) -> set[str]:
    impacted_files = set(changed_files)
    queue = deque(changed_files)

    while queue:
        current_file = queue.popleft()
        for dependent_file in reverse_graph.get(current_file, ()):
            if dependent_file in impacted_files:
                continue
            impacted_files.add(dependent_file)
            queue.append(dependent_file)

    return impacted_files


def _match_repo_file(path_value: str, project_python_files: set[str]) -> str | None:
    normalized = path_value.strip().replace("\\", "/")
    if not normalized:
        return None

    while normalized.startswith("./"):
        normalized = normalized[2:]

    if normalized in project_python_files:
        return normalized

    suffix_matches = [
        file_path
        for file_path in project_python_files
        if normalized.endswith(f"/{file_path}") or normalized.endswith(file_path)
    ]
    if len(suffix_matches) == 1:
        return suffix_matches[0]
    if len(suffix_matches) > 1:
        return max(suffix_matches, key=len)

    return None


def _resolve_item_python_file(item, project_python_files: set[str]) -> str | None:
    item_path = getattr(item, "path", None)
    if item_path:
        matched_file = _match_repo_file(str(item_path), project_python_files)
        if matched_file:
            return matched_file

    item_fspath = getattr(item, "fspath", None)
    if item_fspath:
        matched_file = _match_repo_file(str(item_fspath), project_python_files)
        if matched_file:
            return matched_file

    item_nodeid = getattr(item, "nodeid", "")
    if item_nodeid:
        nodeid_file = item_nodeid.split("::", 1)[0]
        return _match_repo_file(nodeid_file, project_python_files)

    return None
