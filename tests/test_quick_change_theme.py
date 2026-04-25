from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_quick_change_theme(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(By.XPATH, "//*[contains(text(), 'Dark') or contains (text(), 'dark')]").click()

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme.lower() == "dark"

    # browser.find_element(By.XPATH, "//*[contains(text(), 'Light') or contains (text(), 'light')]").click()
