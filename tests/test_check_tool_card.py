import time
from selenium.webdriver.common.by import By



def test_get_url(browser):

    browser.get("https://practicesoftwaretesting.com")

    product_name = browser.find_element(By.XPATH, '//*[@data-test="product-name"]')
    product_name.click()

    add_to_cart = browser.find_element(By.XPATH, '//*[@data-test="add-to-cart"]')
    assert add_to_cart.is_displayed(), "Button is missing"
