import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

standard_themes_values = {
        'dark': 'dark',
        'light': 'none',
        'system': 'system'
    }

def test_quick_change_theme_not_able(browser):
    ActionChains(browser).move_to_element(browser.find_element(By.ID, 'root-action-UserAction')).perform()
    browser.find_element(By.CSS_SELECTOR, 'a.jenkins-dropdown__item[href $= "appearance"]').click()

    ActionChains(browser).move_to_element(browser.find_element(By.ID, 'root-action-UserAction')).perform()
    assert not browser.find_elements(By.ID, 'account-theme-picker'), "Error: Quick theme change block is displayed, when the Appearance page is open"


def test_select_system_theme_by_quick_change(browser):

    ActionChains(browser).move_to_element(browser.find_element(By.ID, 'root-action-UserAction')).perform()

    locator = f'#account-theme-picker > option[value *= "{standard_themes_values.get("system")}"]'
    browser.find_element(By.CSS_SELECTOR, locator).click()

    assert 'System' in browser.find_element(By.CSS_SELECTOR, 'label[for="account-theme-picker"] > span').text


def test_not_apply_change_theme(browser):

    ActionChains(browser).move_to_element(browser.find_element(By.ID, 'root-action-UserAction')).perform()
    browser.find_element(By.XPATH, "//div[contains(@class, 'jenkins-dropdown')]//*[normalize-space()='Appearance']").click()

    browser.find_element(By.XPATH, f'//label[./div[@data-theme = "{standard_themes_values.get("dark")}"]]').click()

    browser.find_element(By.XPATH, f'//a[./span/text()="Profile"]').click()


    browser.find_element(By.XPATH, '//a[span and contains(@href, "appearance")]').click()
    assert browser.find_element(By.TAG_NAME, 'html').get_attribute("data-theme") == standard_themes_values.get("light")