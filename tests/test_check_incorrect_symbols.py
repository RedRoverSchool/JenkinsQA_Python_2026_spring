import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_the_button(browser):
    wait = WebDriverWait(browser, 10)

    new_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/view/all/newJob']")))
    new_item.click()

    input_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="name"]')))
    input_name.send_keys('?, *, /, , ., !, %, $, &, , ;, :')

    error = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="itemname-invalid"]')))
    assert error.is_displayed()
    assert error.text == '» ‘?’ is an unsafe character'

    button_ok = wait.until(EC.presence_of_element_located((By.ID, 'ok-button')))
    assert not button_ok.is_enabled()