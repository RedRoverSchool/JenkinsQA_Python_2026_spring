from collections import defaultdict


def _collect_dependency_aliases(item):
    aliases = {item.nodeid, item.name, item.name.split("[", 1)[0]}

    original_name = getattr(item, "originalname", None)
    if original_name:
        aliases.add(original_name)

    dependency_marker = item.get_closest_marker("dependency")
    if dependency_marker:
        custom_name = dependency_marker.kwargs.get("name")
        if custom_name:
            aliases.add(str(custom_name))

    return aliases


def _collect_dependency_names(item):
    dependency_marker = item.get_closest_marker("dependency")
    if not dependency_marker:
        return ()

    depends = dependency_marker.kwargs.get("depends")
    if not depends:
        return ()
    if isinstance(depends, str):
        return (depends,)

    try:
        return tuple(str(dep_name) for dep_name in depends if dep_name)
    except TypeError:
        return (str(depends),)


def reorder_items_by_dependency(items):
    if len(items) < 2:
        return

    original_index = {item: idx for idx, item in enumerate(items)}
    global_alias_map = defaultdict(list)
    module_alias_map = defaultdict(list)

    for item in items:
        module_id = item.nodeid.split("::", 1)[0]
        aliases = _collect_dependency_aliases(item)

        for alias in aliases:
            global_alias_map[alias].append(item)
            if "::" not in alias:
                module_alias_map[(module_id, alias)].append(item)

    adjacency = {item: set() for item in items}
    indegree = {item: 0 for item in items}

    for item in items:
        module_id = item.nodeid.split("::", 1)[0]
        for dep_name in _collect_dependency_names(item):
            if "::" in dep_name:
                providers = list(global_alias_map.get(dep_name, ()))
                if not providers:
                    providers = [
                        candidate
                        for candidate in items
                        if candidate.nodeid == dep_name or candidate.nodeid.startswith(f"{dep_name}[")
                    ]
            else:
                providers = list(module_alias_map.get((module_id, dep_name), ()))
                if not providers:
                    providers = list(global_alias_map.get(dep_name, ()))

            for provider in providers:
                if provider is item:
                    continue
                if item not in adjacency[provider]:
                    adjacency[provider].add(item)
                    indegree[item] += 1

    queue = [item for item in items if indegree[item] == 0]
    queue.sort(key=original_index.get)

    ordered_items = []
    while queue:
        current_item = queue.pop(0)
        ordered_items.append(current_item)

        newly_ready = []
        for dependent_item in sorted(adjacency[current_item], key=original_index.get):
            indegree[dependent_item] -= 1
            if indegree[dependent_item] == 0:
                newly_ready.append(dependent_item)

        if newly_ready:
            queue = newly_ready + queue

    if len(ordered_items) != len(items):
        seen = set(ordered_items)
        ordered_items.extend(item for item in items if item not in seen)

    items[:] = ordered_items
