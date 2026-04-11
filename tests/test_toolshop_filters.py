import time

from selenium.webdriver.common.by import By


def test_toolshop_filters(browser):
    browser.get("https://practicesoftwaretesting.com/")
    time.sleep(1)
    power_tools_checkbox = browser.find_element(By.CSS_SELECTOR, '[data-test="category-01KNY366MVN0YAXXH9MC8HC1RB"]')

    power_tools_checkbox.click()

    time.sleep(1)
    sheet_sander_product = browser.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
    assert sheet_sander_product.text == "Sheet Sander"
