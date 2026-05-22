import pytest

from pages.home_page import HomePage


def test_new_item_by_button_create_a_job(browser):
    folder_page = (
        HomePage(browser)
        .new_job_click()
        .set_project_name("My Test Job")
        .select_folder_and_ok_click()
        .set_display_name("My Display Name")
        .set_description("My Description")
        .click_save("folder")
    )

    assert folder_page.get_project_name() == "My Display Name"
    assert folder_page.get_config_description() == "My Description"
