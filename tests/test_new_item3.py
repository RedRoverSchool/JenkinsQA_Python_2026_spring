from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize("invalid_name", [
    "my@item",
    "my#item",
    "my$item",
    "my%item",
    "my^item",
    "my&item",
    "my*item",
    "my:item",
    "my;item",
    "my<item>",
    "my?item",
    "my/item",
    "my\item",
    "my[item]",
    "my!item"
])

def test_invalid_input_item_name(browser, invalid_name):
    browser.find_element(By.XPATH, "//a[contains(., 'New Item')]").click()
    input_item_name = browser.find_element(By.ID, "name")

    input_item_name.clear()
    input_item_name.send_keys(invalid_name)
    browser.find_element(By.TAG_NAME, "body").click()

    errors = browser.find_elements(By.CLASS_NAME, "input-validation-message")

    visible_errors = [
        e.text for e in errors
        if e.is_displayed() and e.text.strip() != ""
    ]

    assert len(visible_errors) > 0, \
        f"Ошибка не появилась для значения '{invalid_name}'"

    error = browser.find_element(By.ID, "itemname-invalid")
    assert error.is_displayed(), f"Ошибка не появилась для '{invalid_name}'"