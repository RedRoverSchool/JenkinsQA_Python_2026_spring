import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")


    element_text_input = driver.find_element(By.NAME, "my-text")
    element_text_input.clear()
    element_text_input.send_keys("Тестовый пример")

    element_password = driver.find_element(By.CSS_SELECTOR, "input[name='my-password']")
    element_password.clear()
    element_password.send_keys("Qwery")

    element_textarea = driver.find_element(By.CSS_SELECTOR, "textarea[name='my-textarea']")
    element_textarea.clear()
    element_textarea.send_keys("Текстовый пример")



    time.sleep(2)  # Пауза для наглядности

    assert element_text_input.get_attribute("value") == "Тестовый пример"
    assert element_password.get_attribute("value") == "Qwery"
    assert element_textarea.get_attribute("value") == "Текстовый пример"

finally:
    driver.quit()


