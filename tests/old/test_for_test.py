import time
from selenium.webdriver.common.by import By


# Классы писать не обязательно. Любая тест-функция просто запрашивает фикстуру 'browser'
def test_python_org_title(browser):
    """Тест проверки заголовка страницы"""
    browser.get("https://www.python.org/")
    assert "Python" in browser.title


def test_python_org_search_input(browser):
    """Тест заполнения поля поиска"""
    browser.get("https://www.python.org/")

    search_box = browser.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys("pytest selenium")

    time.sleep(2)  # Пауза для наглядности

    assert search_box.get_attribute("value") == "pytest selenium"