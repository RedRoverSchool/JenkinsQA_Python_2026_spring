import pytest
from pages.home_page import HomePage


LIST_VIEW_NAME = "New_global_view"


@pytest.mark.dependency(depends=["tests/test_pipeline_project_2.py::test_create_pipeline_project"],scope='session')

def test_create_list_view(browser):
    home_page = HomePage(browser)

    new_view_page = (
        home_page
        .click_add_new_view_tab()
        .enter_name(LIST_VIEW_NAME)
        .select_list_view()
    )
    new_view_page.click_create()

    actual_views = home_page.get_view_tab_names()
    expected_order = sorted(actual_views)

    assert "configure" in browser.current_url, f"Expected 'configure' in URL, but got {browser.current_url}"
    assert LIST_VIEW_NAME in actual_views, f"View '{LIST_VIEW_NAME}' not found in {actual_views}"
    assert actual_views == expected_order, (
        f"Tabs order is wrong!\n"
        f"Expected: {expected_order}\n"
        f"Got: {actual_views}")