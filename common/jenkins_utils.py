from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from http.cookiejar import CookieJar
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus
from urllib.request import HTTPCookieProcessor, Request, build_opener

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

try:
    from .project_utils import get_password, get_url, get_user_name
except ImportError:
    from project_utils import get_password, get_url, get_user_name


@dataclass(frozen=True)
class _HttpResponse:
    status_code: int
    body: str


class JenkinsUtils:
    _HEADER_FORM: tuple[str, str] = ("Content-Type", "application/x-www-form-urlencoded")
    _opener = build_opener(HTTPCookieProcessor(CookieJar()))
    _header_authorization: tuple[str, str] | None = None
    _header_crumb: tuple[str, str] | None = None

    @classmethod
    def _request(
        cls,
        method: str,
        url: str,
        headers: list[tuple[str, str]] | None = None,
        body: str | None = None,
    ) -> _HttpResponse:
        data = body.encode("utf-8") if body is not None else None
        request = Request(url=url, data=data, method=method)

        if headers:
            for key, value in headers:
                request.add_header(key, value)

        try:
            with cls._opener.open(request) as response:
                payload = response.read().decode("utf-8", errors="replace")
                return _HttpResponse(status_code=response.status, body=payload)
        except HTTPError as error:
            payload = error.read().decode("utf-8", errors="replace")
            return _HttpResponse(status_code=error.code, body=payload)
        except URLError as error:
            raise RuntimeError(f"HTTP request failed for {url}") from error

    @classmethod
    def _get_http(cls, url: str, headers: list[tuple[str, str]] | None = None) -> _HttpResponse:
        return cls._request("GET", url, headers=headers)

    @classmethod
    def _post_http(cls, url: str, body: str) -> _HttpResponse:
        return cls._request("POST", url, headers=cls._get_default_headers(), body=body)

    @classmethod
    def _get_header_authorization(cls) -> tuple[str, str]:
        if cls._header_authorization is None:
            credentials = f"{get_user_name()}:{get_password()}"
            encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("ascii")
            cls._header_authorization = ("Authorization", f"Basic {encoded_credentials}")

        return cls._header_authorization

    @classmethod
    def _get_header_crumb(cls) -> tuple[str, str]:
        if cls._header_crumb is None:
            json_response = cls._get_http(
                f"{get_url()}crumbIssuer/api/json",
                headers=[cls._get_header_authorization()],
            )
            if json_response.status_code == 403:
                raise RuntimeError(
                    f'Authorization does not work with user: "{get_user_name()}"'
                )
            if json_response.status_code != 200:
                raise RuntimeError("Something went wrong while clearing data")

            crumb_data = json.loads(json_response.body)
            cls._header_crumb = (crumb_data["crumbRequestField"], crumb_data["crumb"])

        return cls._header_crumb

    @classmethod
    def _get_default_headers(cls) -> list[tuple[str, str]]:
        return [cls._HEADER_FORM, cls._get_header_authorization(), cls._get_header_crumb()]

    @classmethod
    def _get_crumb_as_string(cls) -> str:
        crumb_field, crumb_value = cls._get_header_crumb()
        return f"{crumb_field}={crumb_value}"

    @staticmethod
    def _get_substrings_from_page(
        page: str,
        from_substring: str,
        to_substring: str,
        max_substring_length: int = 256,
    ) -> set[str]:
        result: set[str] = set()

        index = page.find(from_substring)
        while index != -1:
            index += len(from_substring)
            end_index = page.find(to_substring, index)

            if end_index != -1 and end_index - index < max_substring_length:
                result.add(page[index:end_index])
            else:
                end_index = index

            index = page.find(from_substring, end_index)

        return result

    @classmethod
    def _get_page(cls, uri: str) -> str:
        page_response = cls._get_http(f"{get_url()}{uri}", headers=cls._get_default_headers())
        if page_response.status_code != 200:
            raise RuntimeError("Something went wrong while clearing data")

        return page_response.body

    @classmethod
    def _delete_by_link(cls, link: str, names: set[str], crumb: str) -> None:
        for name in names:
            cls._post_http(f"{get_url()}{link % name}", crumb)

    @classmethod
    def _reset_theme(cls) -> None:
        url = f"{get_url()}user/{get_user_name()}/appearance/configSubmit"
        json_payload = (
            '{"userProperty0":{"theme":{"value":"0","stapler-class":'
            '"io.jenkins.plugins.thememanager.none.NoOpThemeManagerFactory",'
            '"$class":"io.jenkins.plugins.thememanager.none.NoOpThemeManagerFactory"}}}'
        )
        encoded_json = quote_plus(json_payload)
        body = f"{cls._get_crumb_as_string()}&json={encoded_json}&Submit=Submit&core:apply=true"
        cls._post_http(url, body)

    @classmethod
    def _delete_jobs(cls) -> None:
        main_page = cls._get_page("")
        cls._delete_by_link(
            "job/%s/doDelete",
            cls._get_substrings_from_page(main_page, 'href="job/', '/"'),
            cls._get_crumb_as_string(),
        )

    @classmethod
    def _delete_views(cls) -> None:
        main_page = cls._get_page("")
        cls._delete_by_link(
            "view/%s/doDelete",
            cls._get_substrings_from_page(main_page, 'href="/view/', '/"'),
            cls._get_crumb_as_string(),
        )

        user_name = get_user_name()
        view_page = cls._get_page("me/my-views/view/all/")
        cls._delete_by_link(
            f"user/{user_name}/my-views/view/%s/doDelete",
            cls._get_substrings_from_page(
                view_page,
                f'href="/user/{user_name}/my-views/view/',
                '/"',
            ),
            cls._get_crumb_as_string(),
        )

    @classmethod
    def _delete_users(cls) -> None:
        user_page = cls._get_page("manage/securityRealm/")
        users = cls._get_substrings_from_page(user_page, 'href="user/', '/"')
        users.discard(get_user_name())
        cls._delete_by_link(
            "manage/securityRealm/user/%s/doDelete",
            users,
            cls._get_crumb_as_string(),
        )

    @classmethod
    def _delete_nodes(cls) -> None:
        main_page = cls._get_page("computer/")
        nodes = cls._get_substrings_from_page(main_page, 'href="../computer/', '/" ')
        nodes.discard("(built-in)")
        cls._delete_by_link(
            "manage/computer/%s/doDelete",
            nodes,
            cls._get_crumb_as_string(),
        )

    @classmethod
    def _delete_description(cls, uri: str) -> None:
        cls._get_page("")
        crumb = cls._get_crumb_as_string()
        body = (
            f"description=&Submit=&{crumb}&"
            f'json=%7B%22description%22%3A+%22%22%2C+%22Submit%22%3A+%22%22%2C+%22Jenkins-Crumb%22%3A+%22{crumb}%22%7D'
        )
        cls._post_http(f"{get_url()}{uri}", body)

    @classmethod
    def _delete_main_description(cls) -> None:
        cls._delete_description("submitDescription")

    @classmethod
    def _delete_view_description(cls) -> None:
        cls._delete_description("me/my-views/view/all/submitDescription")

    @classmethod
    def _delete_domains(cls) -> None:
        system_page = cls._get_page("manage/credentials/store/system/")
        cls._delete_by_link(
            "manage/credentials/store/system/domain/%s/doDelete",
            cls._get_substrings_from_page(system_page, '<a href="domain/', '" class'),
            cls._get_crumb_as_string(),
        )

    @classmethod
    def _delete_system_message(cls) -> None:
        crumb = cls._get_crumb_as_string()
        body = (
            f"system_message=&{crumb}&"
            f'json=%7B%22system_message%22%3A%22%22%2C%22Jenkins-Crumb%22%3A%22{crumb}%22%7D'
        )
        cls._post_http(f"{get_url()}manage/configSubmit", body)

    @classmethod
    def clear_data(cls) -> None:
        cls._delete_views()
        cls._delete_jobs()
        cls._delete_users()
        cls._delete_nodes()
        cls._delete_main_description()
        cls._delete_view_description()
        cls._delete_system_message()
        cls._delete_domains()
        cls._reset_theme()

    @staticmethod
    def login(driver: WebDriver, user_name: str | None = None, password: str | None = None) -> None:
        login_user = user_name or get_user_name()
        login_password = password or get_password()

        driver.find_element(By.NAME, "j_username").send_keys(login_user)
        driver.find_element(By.NAME, "j_password").send_keys(login_password)
        driver.find_element(By.NAME, "Submit").click()

    @staticmethod
    def logout(driver: WebDriver) -> None:
        driver.get(f"{get_url()}logout")


def clear_data() -> None:
    JenkinsUtils.clear_data()


def login(driver: WebDriver, user_name: str | None = None, password: str | None = None) -> None:
    JenkinsUtils.login(driver, user_name=user_name, password=password)


def logout(driver: WebDriver) -> None:
    JenkinsUtils.logout(driver)
