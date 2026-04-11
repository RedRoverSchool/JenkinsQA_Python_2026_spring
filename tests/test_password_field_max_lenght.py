from telnetlib import EC
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://www.selenium.dev/selenium/web/web-form.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

def test_password_field_max_lenght(browser):
    browser.get(URL)
    password_field = browser.find_element(By.CSS_SELECTOR, "input[name='my-password']")
    time.sleep(3)
    maxlenght = password_field.get_attribute("maxlength")

    assert maxlenght is None

    long_password = 'a'*100
    time.sleep(3)
    password_field.send_keys(long_password)
    entered_value = password_field.get_attribute("value")
    time.sleep(3)
    assert len(entered_value) == 100

def test_submit_with_long_password(browser):
    browser.get(URL)
    password_field.send_keys(long_password)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    message = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#message"))
    )
    assert message.text == "Recieved!"