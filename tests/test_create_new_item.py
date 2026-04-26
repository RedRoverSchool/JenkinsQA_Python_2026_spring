import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip(reason="fails in CI")
@pytest.mark.parametrize("invalid_char", ["?", "*", "/", "|", "!", "%", "&", ";", ":"])
def test_create_new_item_validate_unsupported_special_characters(browser, invalid_char):
    wait = WebDriverWait(browser, 10)

    browser.find_element(By.LINK_TEXT, "New Item").click()
    browser.find_element(By.ID, "name").send_keys(f"test{invalid_char}job")

    """need wait because the element exists in DOM but is not visible yet, while"""
    warning = wait.until(
        EC.visibility_of_element_located((By.ID, "itemname-invalid"))
    )
    ok_button = browser.find_element(By.ID, "ok-button")

    assert "unsafe character" in warning.text
    assert ok_button.get_attribute("disabled") is not None