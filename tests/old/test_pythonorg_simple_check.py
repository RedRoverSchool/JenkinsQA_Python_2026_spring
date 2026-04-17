import time
from selenium.webdriver.common.by import By


def test_python_org_title_getting_started(browser):
    """Тест проверки заголовка страницы Getting Started раздела About"""
    browser.get("https://www.python.org/")

    button_about = browser.find_element(By.CSS_SELECTOR, "#about > a")
    button_about.click()
    button_about_getting = browser.find_element(By.LINK_TEXT, "Getting Started")
    button_about_getting.click()

    time.sleep(2)  # Пауза для наглядности

    assert "Python For Beginners" in browser.title
