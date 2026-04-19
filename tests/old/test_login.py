from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://www.saucedemo.com")

    (wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='username']")))
        .send_keys("standard_user"))
    browser.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
    browser.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()

    header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    assert header.text == "Products"

def test_invalid_credentials_login(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://www.saucedemo.com")

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='username']"))).send_keys("bad_user")
    browser.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("bad_pass")
    browser.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()

    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "Username and password do not match" in error.text
