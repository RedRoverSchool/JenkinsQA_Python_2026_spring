import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_change_theme_through_appearance_page(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(By.XPATH, "//div[contains(@class, 'jenkins-dropdown')]//*[normalize-space()='Appearance']").click()
    browser.find_element(By.XPATH, "//div[@class='app-theme-picker__item']//*[contains(text(),'Dark') or contains(text(), 'dark')]").click()
    time.sleep(1)

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme.lower() == "dark"