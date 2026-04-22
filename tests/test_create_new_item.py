import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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


def test_create_new_item(browser):
    element_button = browser.find_element(By.CLASS_NAME, "task-icon-link")
    element_button.click()

    input_item_name = browser.find_element(By.ID, 'name')
    input_item_name.send_keys('New_Project')

    select_item_type = browser.find_element(By.CLASS_NAME, 'hudson_model_FreeStyleProject')
    select_item_type.click()

    ok_button = browser.find_element(By.ID, 'ok-button')
    ok_button.click()

    save_button = browser.find_element(By.XPATH, "//*[@value='Save']")
    save_button.click()

    WebDriverWait(browser, 10).until(
        EC.url_contains("/job/")
    )

    time.sleep(2)

    project_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    print(f"Найден заголовок: '{project_title.text}'")
    assert "New_Project" in project_title.text
