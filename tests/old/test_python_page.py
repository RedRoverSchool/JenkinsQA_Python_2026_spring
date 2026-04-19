from selenium import webdriver
from selenium.webdriver.common.by import By

MAIN_PAGE_URL = 'https://www.python.org/'


driver = webdriver.Chrome()

def test_python_page():
    driver.get(MAIN_PAGE_URL)
    driver.implicitly_wait(0.5)

    url_current = driver.current_url

    assert url_current == MAIN_PAGE_URL

