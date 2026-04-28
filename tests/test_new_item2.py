from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize("valid_name", [
    "myitem",
    "MyItem",
    "ITEM",
    "123",
    "0",
    "myitem123",
    "123myitem",
    "myitem123myitem",
    "my-item",
    "-item",
    "item-",
    "my_item",
    "_item",
    "item_",
    "my item",
    " my item",
    "my item ",
    "a" * 255
])

    
def test_valid_input_item_name(browser, valid_name):
    browser.find_element(By.XPATH, "//a[contains(., 'New Item')]").click()
    input_item_name = browser.find_element(By.ID, "name")

    input_item_name.clear()
    input_item_name.send_keys(valid_name)
    browser.find_element(By.TAG_NAME, "body").click()

    error = browser.find_element(By.ID, "itemname-invalid")
    assert not error.is_displayed(), f"Ошибка: {error.text}"




