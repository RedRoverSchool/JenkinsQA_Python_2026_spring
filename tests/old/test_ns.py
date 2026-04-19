import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_python_org_search_input(browser):
    """Тест заполнения поля поиска"""
    browser.get("https://www.python.org/")

    search_box = browser.find_element(By.ID, "id-search-field")
    search_box.clear()
    search_box.send_keys("Job - Python Developer")

    search_button = browser.find_element(By.ID, "submit")
    search_button.click()


    time.sleep(1)  # Пауза для наглядности

    assert "Search" in browser.find_element(By.XPATH,'//*[@id="content"]/div/section/h2').text
    print("✓ Тест пройден успешно!")
