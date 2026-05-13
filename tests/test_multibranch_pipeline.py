import pytest

from pages.home_page import HomePage

old_name = "oldName"
new_name = "newName"

@pytest.mark.dependency()
def test_rename_by_valid_name(browser):

    res = (HomePage(browser)
     .new_item_click()
     .set_project_name(old_name)
     .select_multibranch_and_ok_click()
     .click_submit_button()
     .click_rename_button()
     .fill_rename_field(new_name)
     .click_rename_submit_button()
     .get_project_name())

    assert res == new_name

@pytest.mark.dependency(depends=["test_rename_by_valid_name"])
def test_rename_by_same_name(browser):

    res = (HomePage(browser)
           .click_multibranch_pipeline_job(new_name)
           .click_rename_button()
           .fill_rename_field(new_name)
           .get_same_name_warning_message())

    assert res == "The new name is the same as the current name."

@pytest.mark.dependency(depends=["test_rename_by_same_name"])
def test_rename_by_empty_string(browser):

    res = (HomePage(browser)
     .click_multibranch_pipeline_job(new_name)
     .click_rename_button()
     .fill_rename_field("")
     .get_empty_name_warning_message())

    assert res == "No name is specified"

@pytest.mark.dependency(depends=["test_rename_by_empty_string"])
@pytest.mark.parametrize("invalid_character", ["!", "/", "\\", "?", "%", "*", ":", "|", "<", ">", "#"])
def test_rename_by_invalid_characters(browser, invalid_character):

    res = (HomePage(browser)
     .click_multibranch_pipeline_job(new_name)
     .click_rename_button()
     .fill_rename_field(new_name, invalid_character)
     .get_warning_message(invalid_character))

    assert res == f"‘{invalid_character}’ is an unsafe character"
