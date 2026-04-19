import time


def test_automation_exercise_title(browser):
    """Тест проверки заголовка страницы"""
    browser.get("https://automationexercise.com/")
    assert "Automation Exercise" in browser.title


    time.sleep(2)