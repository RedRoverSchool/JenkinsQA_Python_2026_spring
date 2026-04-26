from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing_extensions import assert_type


def test_disable_active_project(browser):
    wait = WebDriverWait(browser, 10)

    new_item_button = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']")
    new_item_button.click()
    item_name_input = browser.find_element(By.ID, "name")
    item_name_input.send_keys('new')
    item_type = browser.find_element(By.CSS_SELECTOR, "li.hudson_model_FreeStyleProject")
    item_type.click()
    ok_button = browser.find_element(By.XPATH, '//*[@id="ok-button"]')
    ok_button.click()

    wait.until(EC.url_contains("configure"))
    assert 'configure' in browser.current_url

    toggle = browser.find_element(By.CSS_SELECTOR, 'label[for="enable-disable-project"]')
    toggle.click()

    save_button = browser.find_element(By.NAME, "Submit")
    save_button.click()

    warning = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'This project is currently disabled')]")
        )
    )
    assert warning.is_displayed()