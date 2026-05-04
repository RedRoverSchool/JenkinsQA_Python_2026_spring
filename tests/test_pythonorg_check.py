from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_check_news():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org/")

    news_link = driver.find_element(By.LINK_TEXT, "News")
    news_link.click()

    assert "blogs" in driver.current_url

    driver.quit()