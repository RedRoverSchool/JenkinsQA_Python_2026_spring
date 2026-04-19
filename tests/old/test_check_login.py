from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def test_saucedemo_title(browser):
    """Check page title"""
    browser.get(BASE_URL)
    assert "Swag Labs" in browser.title


def test_user_can_login_with_valid_credentials(browser):
    """Check login page with correct username and password"""
    browser.get(BASE_URL)
    username = "standard_user"
    password = "secret_sauce"

    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "login-button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    assert browser.current_url == f"{BASE_URL}inventory.html"