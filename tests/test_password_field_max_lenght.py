from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://www.selenium.dev/selenium/web/web-form.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_password_field_max_length(driver):
    driver.get(URL)
    password_field = driver.find_element(By.CSS_SELECTOR, "input[name='my-password']")
    maxlength = password_field.get_attribute("maxlength")
    assert maxlength is None
    long_password = 'a' * 100
    password_field.send_keys(long_password)
    entered_value = password_field.get_attribute("value")
    assert len(entered_value) == 100

def test_submit_with_long_password(driver):
    driver.get(URL)
    password_field = driver.find_element(By.CSS_SELECTOR, "input[name='my-password']")
    long_password = 'a' * 100
    password_field.send_keys(long_password)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#message"))
    )
    assert message.text == "Received!"