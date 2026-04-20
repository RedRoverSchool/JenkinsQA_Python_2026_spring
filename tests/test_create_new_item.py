import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip
@pytest.mark.parametrize("invalid_char", ["?", "*", "/", "|", "!", "%", "&", ";", ":"])
def test_create_new_item_validate_unsupported_special_characters(browser, invalid_char):
    wait = WebDriverWait(browser, 10)

    browser.find_element(By.LINK_TEXT, "New Item").click()

    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    name_input.clear()
    name_input.send_keys(f"test{invalid_char}job")

    wait.until(
        EC.text_to_be_present_in_element((By.ID, "itemname-invalid"), "unsafe character")
    )
    warning = browser.find_element(By.ID, "itemname-invalid")
    ok_button = browser.find_element(By.ID, "ok-button")

    assert warning.is_displayed()
    assert "unsafe character" in warning.text
    assert ok_button.get_attribute("disabled") is not None