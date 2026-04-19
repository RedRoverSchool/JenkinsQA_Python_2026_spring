from selenium.webdriver.common.by import By


def test_dynamic_click(browser):
    """Тест проверки клика на кнопку"""
    browser.get("https://demoqa.com/buttons")

    simple_button = browser.find_element(By.XPATH, "//button[text()='Click Me']")
    simple_button.click()

    assert "You have done a dynamic click" in browser.page_source
