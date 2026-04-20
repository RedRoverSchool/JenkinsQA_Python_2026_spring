import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def random_characters():
    unsupported_characters = ["?", "*", "/", "|", "!", "%", "&", ";", ":"]
    return random.choice(unsupported_characters)

def test_unsupported_characters(browser):
    wait = WebDriverWait(browser, 2)

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h1")))

    character = random_characters()

    new_item = browser.find_element(By.XPATH, "//a[@it]")
    new_item.click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h1")))

    new_item_field = browser.find_element(By.XPATH, "//input[@name='name']")
    new_item_field.send_keys(character)

    message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='itemname-invalid']"))).text

    assert message == f"» ‘{character}’ is an unsafe character"

    button = browser.find_element(By.XPATH, "//button[@id='ok-button']")

    assert button.is_enabled() is False