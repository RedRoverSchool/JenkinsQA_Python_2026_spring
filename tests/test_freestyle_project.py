from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.home_page import HomePage

FREESTYLE_PROJECT_NAME = "freestyle_project"
DESCRIPTION = "Description Freestyle Project"


@pytest.mark.dependency()
def test_create_freestyle_project(browser):
    project_page=(
        HomePage(browser)
        .click_new_item()
        .set_project_name(FREESTYLE_PROJECT_NAME)
        .select_freestyle_and_ok_click()
        .set_description(DESCRIPTION)
        .click_save()
     )

    assert project_page.get_description() == DESCRIPTION
    assert project_page.get_project_name() == FREESTYLE_PROJECT_NAME


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_enable_delete_workspace_before_build_starts(browser):
    is_selected = (
        HomePage(browser)
        .click_project_name(FREESTYLE_PROJECT_NAME)
        .click_project_configure("freestyle_project")
        .enable_delete_workspace_before_build_starts()
        .click_project_save()
        .click_configure()
        .is_delete_workspace_before_build_starts_selected()
    )

    assert is_selected


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_rename_freestyle_project_page_from_dashboard(browser):
    rename_project_page = (
        HomePage(browser)
        .open_project_dropdown(FREESTYLE_PROJECT_NAME)
        .click_project_rename(FREESTYLE_PROJECT_NAME)
    )

    assert rename_project_page.get_rename_project_page_title() ==  f'Rename Project {FREESTYLE_PROJECT_NAME}'


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_rename_freestyle_project_page_from_project_page(browser):
    rename_project_page = (
        HomePage(browser)
        .click_project_name(FREESTYLE_PROJECT_NAME)
        .click_rename_project()
    )

    assert rename_project_page.get_rename_project_page_title() ==  f'Rename Project {FREESTYLE_PROJECT_NAME}'


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
@pytest.mark.parametrize("special_character", ['?', '*', '/', '!'])
def test_special_characters_in_rename_field(browser, special_character):
    rename_project_page = (
        HomePage(browser)
        .click_project_name(FREESTYLE_PROJECT_NAME)
        .click_rename_project()
        .clear_rename_field()
        .set_new_project_name(special_character)
    )

    error_message = f"‘{special_character}’ is an unsafe character"
    assert rename_project_page.get_rename_project_error_message() == error_message


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_blank_rename_field(browser):
    rename_project_page = (
        HomePage(browser)
        .click_project_name(FREESTYLE_PROJECT_NAME)
        .click_rename_project()
        .clear_rename_field()
        .click_main_panel()
    )

    error_message = 'No name is specified'
    assert rename_project_page.get_rename_project_error_message() == error_message
