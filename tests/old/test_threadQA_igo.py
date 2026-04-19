from selenium import webdriver
from selenium.webdriver.common.by import By

def test_text_area():
    driver = webdriver.Chrome()

    driver.get("https://lms.threadqa.ru/xpath-practice-hub")
    driver.implicitly_wait(2.5)

    mnogo_str = driver.find_element(By.CSS_SELECTOR, "[data-testid='comment-field']")

    assert mnogo_str.get_attribute("placeholder") == "Введите ваш комментарий..."

    test_text_str = "три кота\nтри хвоста \nМяу"
    mnogo_str.send_keys(test_text_str)
    driver.implicitly_wait(2.5)
    assert mnogo_str.get_attribute("value") == test_text_str, "Введенный текст  совпадает с ожидаемым"
    print("Тест пройден: плейсхолдер и ввод текста работают корректно!")

    driver.quit()
