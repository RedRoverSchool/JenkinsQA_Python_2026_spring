from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_theme_dropdown(browser):
    profile_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root-action-UserAction']"))
    )
    actions = ActionChains(browser)
    actions.move_to_element(profile_element).perform()

    theme_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='account-theme-picker']"))
    )
    theme_element.click()

    dark_option = theme_element.find_element(By.XPATH, "//option[@value='dark']")
    dark_option.click()

    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//html[@data-theme='dark']"))
    )

    theme_select = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "select#account-theme-picker"))
    )
    theme_element.click()
    light_option = theme_element.find_element(By.XPATH, "//option[text()='Light']")
    light_option.click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//html[@data-theme='none']"))
    )


