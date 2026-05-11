import pytest

from pages.home_page import HomePage

FREESTYLE_PROJECT_NAME = "freestyle_project"
DESCRIPTION = "Description Freestyle Project"

@pytest.mark.dependency()
def test_create_freestyle_project(browser):
    project_page = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(FREESTYLE_PROJECT_NAME)
        .select_freestyle_and_ok_click()
        .set_description(DESCRIPTION)
        .save()
    )

    assert project_page.get_description() == DESCRIPTION
    assert project_page.get_project_name() == FREESTYLE_PROJECT_NAME
