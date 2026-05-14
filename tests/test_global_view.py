import pytest
from pages.home_page import HomePage
LIST_VIEW_NAME = "New_global_view"

@pytest.mark.dependency(depends=["tests/test_pipeline_project_2.py::test_create_pipeline_project"],
    scope='session'
)
def test_create_list_view(browser):
    home_page = HomePage(browser)

    new_view_page = (
        home_page
        .click_add_new_view_tab()
        .enter_name(LIST_VIEW_NAME)
        .select_list_view()
    )

    assert "newView" in browser.current_url
    assert new_view_page.is_create_button_enabled()

    new_view_page.click_create()

    assert "configure" in browser.current_url, f"Expected 'configure' in URL, but got {browser.current_url}"