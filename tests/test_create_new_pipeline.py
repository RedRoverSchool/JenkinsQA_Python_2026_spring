import pytest

from pages.home_page import HomePage

PIPELINE_NAME = "Test Pipeline"
DESCRIPTION = "Description Pipeline"


@pytest.mark.dependency()
def test_create_new_pipeline(browser):
    project_page = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(PIPELINE_NAME)
        .select_pipeline_and_ok_click()
        .set_description(DESCRIPTION)
        .save()
    )

    assert project_page.get_description() == DESCRIPTION
    assert project_page.get_project_name() == PIPELINE_NAME

