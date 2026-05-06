import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ITEM_NAME = "Test Pipeline"


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 5)


@pytest.mark.dependency()
def test_create_new_pipeline(browser, wait):
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()
    browser.find_element(By.CSS_SELECTOR, "button#ok-button[disabled]")
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(ITEM_NAME)
    browser.find_element(By.XPATH, "//li[.//span[normalize-space()='Pipeline']]").click()
    browser.find_element(By.CSS_SELECTOR, "button#ok-button").click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='Apply']"))
    ).click()
    browser.find_element(By.CSS_SELECTOR, "a.app-jenkins-logo").click()

    all_items = browser.find_elements(By.CSS_SELECTOR, "a.jenkins-table__link")
    all_itemnames = [item.text for item in all_items]

    assert ITEM_NAME in all_itemnames


@pytest.mark.dependency(depends=["test_create_new_pipeline"])
def test_message_field_cannot_be_empty(browser, wait):
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("")
    browser.find_element(By.XPATH, "//li[.//span[normalize-space()='Pipeline']]").click()
    message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='itemname-required']"))
    )

    assert message.text == "» This field cannot be empty, please enter a valid name"


@pytest.mark.dependency(depends=["test_message_field_cannot_be_empty"])
def test_message_not_allowed_name(browser, wait):
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(".")
    message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='itemname-invalid']"))
    )

    assert message.text == "» “.” is not an allowed name"


@pytest.mark.dependency(depends=["test_message_not_allowed_name"])
def test_message_unsafe_character(browser, wait):
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()
    for _ in ["?", "*", "/", "!", "%", "$", "&", ";", ":"]:
        browser.find_element(By.CSS_SELECTOR, "input#name").clear()
        browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(f"{_}")
        message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[@id='itemname-invalid']"))
        )

        assert message.text == f"» ‘{_}’ is an unsafe character"


@pytest.mark.dependency(depends=["test_message_unsafe_character"])
def test_message_job_already_exists(browser, wait):
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[normalize-space()='New Item']]"))
    ).click()
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(ITEM_NAME)
    message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='itemname-invalid']"))
    )

    assert message.text == "» A job already exists with the name ‘Test Pipeline’"
