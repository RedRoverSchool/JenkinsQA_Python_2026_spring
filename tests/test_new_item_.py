from selenium.webdriver.common.by import By


def test_new_item_(browser):
    browser.find_element(By.XPATH, "//a[.//span[normalize-space()='New Item']]").click()
    browser.find_element(By.CSS_SELECTOR, "button#ok-button[disabled]")
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("")
    browser.find_element(By.XPATH, "//li[.//span[normalize-space()='Pipeline']]").click()
    browser.find_element(
        By.XPATH,
        "//div[@id='itemname-required' and normalize-space()='» This field cannot be empty, please enter a valid name']"
    )
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(".")
    browser.find_element(
        By.XPATH, "//div[@id='itemname-invalid' and normalize-space()='» “.” is not an allowed name']"
        )
    browser.find_element(By.CSS_SELECTOR, "input#name").clear()
    for _ in ["?", "*", "/", "!", "%", "$", "&", ";", ":"]:
        browser.find_element(By.CSS_SELECTOR, "input#name").send_keys(f"{_}")
        browser.find_element(
            By.XPATH, f"//div[@id='itemname-invalid' and normalize-space()='» ‘{_}’ is an unsafe character']"
        )
        browser.find_element(By.CSS_SELECTOR, "input#name").clear()
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("Test Pipeline")
    browser.find_element(By.XPATH, "//li[.//span[normalize-space()='Pipeline']]").click()
    browser.find_element(By.CSS_SELECTOR, "button#ok-button").click()
    browser.find_element(By.XPATH, "//button[@name='Apply']").click()
    browser.find_element(By.CSS_SELECTOR, "a.app-jenkins-logo").click()
    browser.find_element(By.XPATH, "//a[.//span[normalize-space()='New Item']]").click()
    browser.find_element(By.CSS_SELECTOR, "input#name").send_keys("Test Pipeline")
    browser.find_element(By.CSS_SELECTOR, "button#ok-button[disabled]")
    browser.find_element(
        By.XPATH, "//div[@id='itemname-invalid' and normalize-space()='» A job already exists with the name ‘Test Pipeline’']"
    )
    browser.find_element(By.CSS_SELECTOR, "a.app-jenkins-logo").click()

    result = browser.find_element(By.XPATH, "//a[.//span[normalize-space()='Test Pipeline']]").text
    assert result == "Test Pipeline"
