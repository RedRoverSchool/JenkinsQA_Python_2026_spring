import pytest
import os
from pages.home_page import HomePage

CURRENT_USER_NAME = os.getenv("JENKINS_USERNAME")
AVAILABLE_ITEMS = [
    "my-views",
    "account",
    "appearance",
    "preferences",
    "security",
    "experiments",
    "credentials",
]


def test_profile_icon_click(browser):
    result_page = HomePage(browser).click_profile_icon_in_header().get_current_url()

    assert CURRENT_USER_NAME in result_page


@pytest.mark.parametrize("item", AVAILABLE_ITEMS)
def test_profile_icon_dropdown_menu_item_click(browser, item):
    result_page = (
        HomePage(browser)
        .click_item_in_profile_icon_dropdown_menu(item)
        .get_current_url()
    )

    assert item in result_page
