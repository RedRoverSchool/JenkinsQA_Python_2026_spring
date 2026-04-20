import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def open_new_item_form(browser):
    create_a_new_item = browser.find_element(By.CSS_SELECTOR, "div.task")
    create_a_new_item.click()

def test_new_item_(browser):
    open_new_item_form(browser)
    new_item = browser.find_element(By.CSS_SELECTOR, "div#add-item-panel>h1")
    assert new_item.text == "New Item"

def test_btn_ok_disabled(browser):
    open_new_item_form(browser)
    btn_ok = browser.find_element(By.CSS_SELECTOR, "button#ok-button")
    assert not btn_ok.is_enabled()

def test_btn_ok_enabled(browser):
    open_new_item_form(browser)
    input_name = browser.find_element(By.CSS_SELECTOR, "input#name")
    pipeline = browser.find_element(By.XPATH, "//span[@class='label' and text()='Pipeline']")
    warning_message = browser.find_element(By.CSS_SELECTOR, "div#itemname-required")
    pipeline.click()
    input_name.click()
    assert "This field cannot be empty, please enter a valid name" in warning_message.text

def test_allowed_name(browser):
    open_new_item_form(browser)
    input_name = browser.find_element(By.CSS_SELECTOR, "input#name")
    input_name.send_keys(".")
    time.sleep(1)
    warning_message = browser.find_element(By.CSS_SELECTOR, "div#itemname-invalid")
    assert "is not an allowed name" in warning_message.text







