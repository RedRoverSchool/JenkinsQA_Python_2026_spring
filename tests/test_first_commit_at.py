from selenium.webdriver.common.by import By


def test_text_main_page(browser):
    """Тест проверки текстов на главной странице
       Тест работы с гитом"""

    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")
    assert label.text == "Welcome to Jenkins!"

    paragraph = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > p")
    assert "This page" in paragraph.text

    h2_1 = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block h2")
    assert h2_1.text == "Start building your software project"

