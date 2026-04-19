from selenium.webdriver.common.by import By

def test_codewars_com_title(browser):
    """Тест проверки заголовка страницы"""
    browser.get("https://www.codewars.com/")
    assert "Codewars" in browser.title