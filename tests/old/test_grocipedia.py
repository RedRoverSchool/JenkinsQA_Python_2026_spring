from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_find_element():
    driver = webdriver.Chrome()
    driver.get("https://grokipedia.com/")

    search_input = driver.find_element(By.XPATH, '//*[@id="search-input"]')
    search_input.send_keys("python")

    search_button = driver.find_element(By.XPATH, '//*[@id="search-submit"]')
    search_button.click()
    # time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '/html/body/main/div[3]/a[1]/div/div[2]/div/span')
    submit_button.click()
    time.sleep(2)

    page_header = driver.find_element(By.XPATH, '//*[@id="python_efteling"]')

    assert page_header.text ==  'Python (Efteling)'
