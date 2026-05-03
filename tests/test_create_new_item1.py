import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.dependency()
def test_new_item(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()

    ok_button = browser.find_element(By.CSS_SELECTOR, "button#ok-button")
    assert not ok_button.is_enabled()

    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("Test Pipeline")
    browser.find_element(By.XPATH, "//li[.//span[normalize-space()='Pipeline']]").click()
    browser.find_element(By.CSS_SELECTOR, "button#ok-button").click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='Apply']"))
    ).click()
    browser.find_element(By.CSS_SELECTOR, "a.app-jenkins-logo").click()

    all_items = browser.find_elements(By.CSS_SELECTOR, "a.jenkins-table__link")
    all_itemnames = [item.text for item in all_items]
    assert "Test Pipeline" in all_itemnames


@pytest.mark.dependency(depends=["test_new_item"])
def test_new_item_duplicate(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()

    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("Test Pipeline")
    message_job_already_exists = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div[@id='itemname-invalid' and normalize-space()='» A job already exists with the name ‘Test Pipeline’']"))
    )
    assert message_job_already_exists, "Не появилось сообщение: A job already exists"
    browser.find_element(By.CSS_SELECTOR, "input#name").clear()


@pytest.mark.dependency(depends=["test_new_item_duplicate"])
def test_new_item_invalid_name(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()

    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("")
    browser.find_element(By.XPATH, "//li[.//span[normalize-space()='Pipeline']]").click()
    message_field_cannot_be_empty = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div[@id='itemname-required' and normalize-space()='» This field cannot be empty, please enter a valid name']"))
    )
    assert message_field_cannot_be_empty, "Не появилось сообщение: This field cannot be empty"

    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(".")
    message_not_allowed_name = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='itemname-invalid' and contains(text(), 'is not an allowed name')]"))
    )
    assert message_not_allowed_name, "Не появилось сообщение: '.' is not an allowed name"
    browser.find_element(By.CSS_SELECTOR, "input#name").clear()

    for _ in ["?", "*", "/", "!", "%", "$", "&", ";", ":"]:
        browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(f"{_}")
        message_unsafe_character = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[@id='itemname-invalid' and normalize-space()='» ‘{_}’ is an unsafe character']"))
        )
        assert message_unsafe_character, f"Не появилось сообщение: '» ‘{_}’ is an unsafe character']"
        browser.find_element(By.CSS_SELECTOR, "input#name").clear()
