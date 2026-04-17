import time

from selenium.webdriver.common.by import By


def test_toolshop_search(browser):
    browser.get("https://practicesoftwaretesting.com/")

    time.sleep(1)
    search_area = browser.find_element(By.CSS_SELECTOR, '[data-test=search-query]')
    search_submit = browser.find_element(By.CSS_SELECTOR, '[data-test=search-submit]')

    search_area.send_keys("Thor")
    search_submit.click()

    time.sleep(1)
    product_name = browser.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
    assert product_name.text == "Thor Hammer"
