import pytest
from pages.home_page import HomePage
from tests.test_folder import FOLDER_NAME

@pytest.mark.dependency()
def test_create_folder(browser):
    project_names_list = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .click_save()
        .go_home_page()
        .get_project_names_list()
    )

    assert len(project_names_list) > 0
    assert project_names_list[0] == FOLDER_NAME

@pytest.mark.dependency(depends=['test_create_folder'])
def test_folder_apply_button(browser):
    apply_result = (
        HomePage(browser)
        .click_project_name(FOLDER_NAME, 'folder')
        .click_project_configure('folder')
        .set_display_name("Display_name")
        .click_apply()
        .get_notification_saved()
    )

    assert apply_result == "Saved"
    assert "configure" in browser.current_url, "Apply применяется, редиректа нет"

@pytest.mark.dependency(depends=['test_create_folder'])
def test_folder_save_button(browser):
    save_result = (HomePage(browser)
        .click_project_name(FOLDER_NAME, 'folder')
        .click_project_configure('folder')
        .set_display_name("Display_name")
        .click_save('folder')
    )

    assert "configure" not in browser.current_url, "Save button redirected to the main page"
