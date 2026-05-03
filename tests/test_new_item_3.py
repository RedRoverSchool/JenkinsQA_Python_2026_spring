import time
from selenium.webdriver.common.by import By
import random

invalid_character = ['?', '*', '/', '!', '%', '$', '&', ';', ':', '@', '>', '']
def test_validate_invalid_item_name(browser):
    browser.find_element(By.XPATH, "//a[.//span[text()='New Item']]").click()
    input_invalid_char = random.choice(invalid_character)
    if input_invalid_char != '':
        browser.find_element(By.XPATH, "//input[@name='name']").send_keys(input_invalid_char)
    browser.find_element(By.XPATH, "//div[@id='page-body']").click()
    time.sleep(1)

    if input_invalid_char in ['', ' ']:
        locator = "//div[@id='itemname-required']"
        expected = "» This field cannot be empty, please enter a valid name"

    else:
        locator = "//div[@id='itemname-invalid']"
        expected = f"» ‘{input_invalid_char}’ is an unsafe character"

    result = browser.find_element(By.XPATH, locator).text
    assert expected in result
