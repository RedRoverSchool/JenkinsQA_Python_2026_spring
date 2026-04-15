import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dynamic_controls"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_enable_disable_input(driver):
    driver.get(URL)          # 1. Открывает страницу

    enable_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")
    enable_button.click()    # 2.Ищем кнопку Enable и кликаем её

    input_field = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input"))
    )                       # 3. ждем, когда поле ввода станет кликабельным

    input_field.send_keys("Hello") # 4. Вводим текст "Hello"

    disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")
    disable_button.click() # 5. Кликаем кнопку "Disable" (теперь она та же кнопка, но текст изменился)

    WebDriverWait(driver, 5).until(
        lambda d: input_field.get_attribute("disabled") is not None
    )                      # 6. Проверяем, что поле ввода disabled
    assert input_field.get_attribute("disabled") is not None
                           # Ждём, пока атрибут disabled появится.