import time
from selenium.webdriver.common.by import By

def test_products_link(browser):
    browser.get("https://automationexercise.com/")
    products_link = browser.find_element(By.CSS_SELECTOR,'a[href="/products"]')
    products_link.click()
    time.sleep(2)
    center_title = browser.find_element(By.CSS_SELECTOR, 'h2.title.text-center')

    assert center_title.text == "ALL PRODUCTS"

def test_woman_category_list(browser):
    browser.get("https://automationexercise.com/")

    women_item = browser.find_element(By.XPATH,"//div[@id='Women']")
    women_link = browser.find_element(By.XPATH, "//div[@id='Women']/..")
    women_panel_link = browser.find_elements(By.CSS_SELECTOR, "#Women li a")

    assert women_item.get_attribute("class") == "panel-collapse collapse"

    women_link.click()
    texts = [element.get_attribute('textContent') for element in women_panel_link]

    assert texts == ["Dress ", "Tops ", "Saree "]