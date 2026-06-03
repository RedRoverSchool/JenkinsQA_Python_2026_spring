from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from conftest import browser
from pages.home_page import HomePage

PIPELINE_NAME = "test_1"


@pytest.mark.dependency()
def test_create_pipeline_project(browser):
    created_pipeline_name = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(PIPELINE_NAME)
        .select_pipeline_and_ok_click()
        .click_save()
        .go_home_page()
        .get_created_project_name(PIPELINE_NAME)
    )
    assert created_pipeline_name == PIPELINE_NAME


@pytest.mark.dependency(depends=["test_create_pipeline_project"])
def test_add_description_pipeline(browser):
    text_description = "Description here"

    added_description = (
        HomePage(browser)
        .click_project_name(PIPELINE_NAME)
        .click_add_description_link()
        .add_description(text_description)
        .get_description()
    )
    assert added_description == text_description

@pytest.mark.dependency(depends=["test_create_pipeline_project"])
@pytest.mark.parametrize("special_character", ['?', '*', '/', '!'])
def test_special_characters_in_rename_pipeline(browser, special_character):
    rename_project_page = (
        HomePage(browser)
        .click_project_name(PIPELINE_NAME)
        .click_rename_project()
        .clear_rename_field()
        .set_new_project_name(special_character)
    )

    error_message = f"‘{special_character}’ is an unsafe character"
    assert rename_project_page.get_rename_project_error_message() == error_message
