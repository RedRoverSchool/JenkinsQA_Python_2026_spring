import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_toolshop_filters(browser):
    browser.get("https://practicesoftwaretesting.com/")
    time.sleep(1)
    power_tools_checkbox = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//label[contains(normalize-space(.), "Power Tools")]//input[@type="checkbox"]'
        ))
    )

    power_tools_checkbox.click()

    time.sleep(1)
    sheet_sander_product = browser.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
    assert sheet_sander_product.text == "Sheet Sander"
