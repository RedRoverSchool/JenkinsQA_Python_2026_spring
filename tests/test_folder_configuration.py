import pytest
from pages.home_page import HomePage

FOLDER_NAME = "TestFolder"
DISPLAY_NAME = "Display Folder"


@pytest.mark.dependency()
def test_add_display_name_to_folder(browser):
    project_names_list = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .click_save()
        .click_project_configure("folder")
        .set_display_name(DISPLAY_NAME)
        .click_save()
        .go_home_page()
        .get_project_names_list()
    )

    assert len(project_names_list) > 0
    assert project_names_list[0] == DISPLAY_NAME
