import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--user-data-dir=/tmp/chrome-test-profile")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def open_site(browser):
    browser.get("https://www.saucedemo.com")

@pytest.fixture
def logged_in(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element("id", "user-name").send_keys("standard_user")
    browser.find_element("id", "password").send_keys("secret_sauce")
    browser.find_element("id", "login-button").click(),


def test_login_success(browser, logged_in):
    title = browser.find_element("class name", "title").text
    assert title == "Products"

def test_login_wrong_password(browser):
    browser.find_element("id", "user-name").send_keys("standard_user")
    browser.find_element("id", "password").send_keys("wrong_password")
    browser.find_element("id", "login-button").click(),
    error = browser.find_element("class name", "error-message-container").text
    assert "Epic sadface" in error

def test_login_empty_fields(browser):
    browser.find_element("id", "login-button").click()
    error = browser.find_element("class name", "error-message-container").text
    assert "Epic sadface" in error

def test_e2e_purchase(browser, logged_in):
    browser.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    browser.find_element("class name", "shopping_cart_link").click()
    item = browser.find_element("class name", "inventory_item_name").text

    assert item == "Sauce Labs Backpack"
    browser.find_element("id", "checkout").click()

    browser.find_element("id", "first-name").send_keys("John")
    browser.find_element("id", "last-name").send_keys("Doe")
    browser.find_element("id", "postal-code").send_keys("12345")
    browser.find_element("id", "continue").click()

    order_item = browser.find_element("class name", "inventory_item_name").text
    assert order_item == "Sauce Labs Backpack"

    browser.find_element("id", "finish").click()
    confirmation = browser.find_element("class name", "complete-header").text
    assert confirmation == "Thank you for your order!"
