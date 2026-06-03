import pytest
from pages.home_page import HomePage

SEARCH_PARTIAL = 't'
SEARCH_EXACT = 'Appearance'
SEARCH_LOAD_STATISTICS = 'Load Statistics'


@pytest.mark.dependency()
def test_checking_dropdown_partial_match(browser):
    items = (
        HomePage(browser)
        .click_manage_gear()
        .search_field(SEARCH_PARTIAL)
        .get_result_items_containing(SEARCH_PARTIAL)
    )

    assert len(items) > 1


@pytest.mark.dependency(depends=["test_checking_dropdown_partial_match"])
def test_checking_dropdown_full_match(browser):
    item_text = (
        HomePage(browser)
        .click_manage_gear()
        .search_field(SEARCH_EXACT)
        .get_exact_result_item_text(SEARCH_EXACT)
    )

    assert item_text == SEARCH_EXACT


# @pytest.mark.skip(reason="ER_10.002.03")
def test_clear_search_field_and_verify_empty(browser):
    page = HomePage(browser).click_manage_gear()

    (
        page
        .clear_field_keyboard()
        .search_field(SEARCH_LOAD_STATISTICS)
        .clear_field_method()
    )

    assert page.get_field_value() == ''
