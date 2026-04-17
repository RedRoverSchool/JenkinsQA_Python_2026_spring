import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_toolshop_filters(browser):
    browser.get("https://practicesoftwaretesting.com/")
    wait = WebDriverWait(browser, 10)

    power_tools_checkbox = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//label[contains(normalize-space(.), "Power Tools")]//input[@type="checkbox"]'
        ))
    )

    power_tools_checkbox.click()

    sheet_sander_product = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            '//h5[@data-test="product-name" and normalize-space()="Sheet Sander"]'
        ))
    )
    assert sheet_sander_product.text == "Sheet Sander"
