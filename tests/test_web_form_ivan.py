import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.selenium.dev/selenium/web/web-form.html"


def test_text_input_and_submit(browser):
    """
    Тест 1: Ввод текста в поле "Textarea" и нажатие на кнопку "Submit"
    """
    # Переход на страницу тестируемого сайта после авторизации в Jenkins
    browser.get(base_url)

    # Ожидаем, что появилось поле ввода
    text_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "my-textarea"))
    )

    # Ввод текста в поле "Textarea"
    test_value = "Мой первый тест в жизни!"
    text_field.send_keys(test_value)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    # Проверяем результат: После отправки переходим на следующую страницу браузера,
    # видим, что URL изменился или появился элемент с результатом
    result_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    # Вывод текста в консоль
    print(result_message.text)

    assert result_message.is_displayed(), "Сообщение об успешной отправке не появилось"
    assert "Received!" in result_message.text, "Введённый текст не отобразился в результате"


def test_disabled_input_has_placeholder_and_is_readonly(browser):
    """
    Тест 2: Проверка disabled input: наличие placeholder + недоступность редактирования
    """
    browser.get(base_url)

    # находим disabled поле через CSS-селектор
    disabled_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "my-disabled"))
    )

    # проверяем наличие placeholder
    placeholder = disabled_input.get_attribute("placeholder")
    assert placeholder, "У disabled input отсутствует атрибут placeholder"

    # проверяем, что поле действительно заблокировано
    assert not disabled_input.is_enabled(), "Поле должно быть disabled, но is_enabled() вернул True"
    print("Поле Disabled input заблокировано!")