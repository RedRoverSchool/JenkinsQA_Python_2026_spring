import pytest

from conftest import browser
from pages.home_page import HomePage

LIST_VIEW_NAME = "New_global_view_name"
REMAINING_PRECONDITION_NAMES = ["1_New_global_view_name", "new_global_view_name"]
TARGET_VIEW_NAME = "A_New_view"

@pytest.fixture(scope="function")
def setup_precondition_pipeline(browser):
    HomePage(browser).go_home_page()
    if not HomePage(browser).is_project_exist("test_1"):
        (HomePage(browser)
            .click_new_item()
            .set_project_name("test_1")
            .select_pipeline_and_ok_click()
            .click_save()
            .go_home_page())

@pytest.mark.dependency()
def test_view_type_selection_options(browser,setup_precondition_pipeline):
    new_view_page = (
        HomePage(browser)
        .click_add_new_view_tab()
    )

    assert new_view_page.is_list_view_displayed(), "The 'List View' radio button is not displayed!"
    assert new_view_page.is_my_view_displayed(), "The 'My View' radio button is not displayed!"
    assert new_view_page.is_create_button_disabled(), "The 'Create' button should be disabled by default"

@pytest.mark.dependency(depends=["test_view_type_selection_options"])
def test_creation_button_displayed_with_valid_name_only(browser):
    new_view_page = (
        HomePage(browser)
        .click_add_new_view_tab()
        .set_view_name(LIST_VIEW_NAME)
    )

    assert new_view_page.is_create_button_disabled(), (
        f"The 'Create' button was unlocked after entering a name '{LIST_VIEW_NAME}', "
        f"although the View type has not yet been selected!"
    )

@pytest.mark.dependency(depends=["test_creation_button_displayed_with_valid_name_only"])
def test_successful_creation_of_list_view(browser):
    (HomePage(browser)
    .click_add_new_view_tab()
    .set_view_name(LIST_VIEW_NAME)
    .select_list_view()
    .click_create())

    assert "configure" in browser.current_url, (
        f"The user was not redirected to the configuration page! "
        f"Current URL: {browser.current_url}"
    )

@pytest.fixture()
def create_remaining_precondition_views(browser):
    for name in REMAINING_PRECONDITION_NAMES:
        (HomePage(browser)
         .click_add_new_view_tab()
         .set_view_name(name)
         .select_list_view()
         .click_create()
         .click_save())
    return browser

@pytest.mark.dependency(depends=["test_successful_creation_of_list_view"])
def test_displaying_and_sorting_of_created_views_in_tab_bar(create_remaining_precondition_views):
    (HomePage(create_remaining_precondition_views)
    .click_add_new_view_tab()
    .set_view_name(TARGET_VIEW_NAME)
    .select_list_view()
    .click_create()
    .click_save()
)
    actual_view = HomePage(create_remaining_precondition_views).get_view_tab_names()
    expected_order = sorted(actual_view)

    assert LIST_VIEW_NAME in actual_view, f"View '{LIST_VIEW_NAME}' not found in {actual_view}"
    assert actual_view == expected_order, (
    f"Tabs order is wrong!\n"
    f"Expected: {expected_order}\n"
    f"Got: {actual_view}")
