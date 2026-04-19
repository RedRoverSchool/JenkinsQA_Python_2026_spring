from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_kirill_input():
    param_word = "123456"
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    time.sleep(2)

    number_input = driver.find_element(By.NAME, "number_input")

    number_input.send_keys(param_word)

    submit_button = driver.find_element(By.NAME, "submit_input")

    submit_button.click()

    time.sleep(2)
    current_url = driver.current_url

    assert param_word in current_url

def test_jana_product_title_matches_between_plp_and_pdp():
    """Title на странице PLP соответствует title на странице PDP"""
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&ref=nav_em__nav_desktop_sa_intl_clothing_0_2_13_2")

    time.sleep(2)

    product_title_link = driver.find_element(By.CSS_SELECTOR, 'a.a-link-normal')
    product_title_plp = driver.find_element(By.CSS_SELECTOR, 'a.a-link-normal h2 span').text

    time.sleep(2)

    product_title_link.click()

    product_title_pdp = driver.find_element(By.ID, "productTitle").text

    assert product_title_plp == product_title_pdp

    driver.quit()







