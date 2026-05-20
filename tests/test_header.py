from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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


def test_header_quick_change_theme(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(
        By.XPATH, "//*[contains(text(), 'Dark') or contains (text(), 'dark')]"
    ).click()

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme.lower() == "dark"


def test_header_change_theme_through_appearance_page(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(
        By.XPATH,
        "//div[contains(@class, 'jenkins-dropdown')]//*[normalize-space()='Appearance']",
    ).click()
    browser.find_element(
        By.XPATH,
        "//div[@class='app-theme-picker__item']//*[contains(text(),'Dark') or contains(text(), 'dark')]",
    ).click()
    browser.find_element(By.XPATH, "//*[@class='jenkins-button apply-button']").click()

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme.lower() == "dark"


def test_profile_icon_click(browser):
    result_heading = HomePage(browser).click_profile_icon_in_header().get_heading()

    assert CURRENT_USER_NAME in result_heading


@pytest.mark.parametrize("item", AVAILABLE_ITEMS)
def test_profile_icon_dropdown_menu_item_click(browser, item):
    result_url = (
        HomePage(browser)
        .click_item_in_profile_icon_dropdown_menu(item)
        .get_current_url()
    )
    print(result_url)
    assert f"/{item}" in result_url
