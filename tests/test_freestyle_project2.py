import pytest

from pages import base_project_page
from pages.home_page import HomePage


FREESTYLE_PROJECT_NAME = "Test_Freestyle"
DESCRIPTION = "Test description"
JOB_TYPE = "freestyle_project"

@pytest.mark.dependency
def test_create_freestyle_project(browser):
    freestyle_job_page = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FREESTYLE_PROJECT_NAME)
        .select_freestyle_and_ok_click()
        .click_save(JOB_TYPE)
    )

    assert freestyle_job_page.get_project_name() == FREESTYLE_PROJECT_NAME


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_description_preview(browser):
    freestyle_config_page = (
        HomePage(browser)
        .open_project_dropdown(FREESTYLE_PROJECT_NAME)
        .click_configure_link()
        .set_description(DESCRIPTION)
        .click_preview_button()
    )

    assert freestyle_config_page.is_preview_textarea_displayed()
    assert freestyle_config_page.get_preview_textarea_text() == freestyle_config_page.get_description_text()
