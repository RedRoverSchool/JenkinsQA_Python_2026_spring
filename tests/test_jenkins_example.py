import time
from selenium.webdriver.common.by import By

def test_welcome(browser):
    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")

    assert label.text == "Welcome to Jenkins!"
