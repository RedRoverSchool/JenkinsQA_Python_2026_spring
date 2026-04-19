import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=\"useragent\"")
    options.add_argument("--disable-cache") # очистка кэша
    options.add_argument("--incognito") # тестировать страницу в режиме инкогнито
    options.add_argument("--headless=new") # режим, в котором мы вообще не получаем графического отображения
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def sauce_site(driver):
    driver.get("https://bfkh.ru/")


# тап по иконке открывает модальное окно "Создать аккаунт"
def test_con_header_user(driver: WebDriver, sauce_site):
    icon_header_user = driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile")
    assert icon_header_user.is_displayed(), "Иконка пользователя не найдена"
    print("Иконка пользователя отображается на странице")



# в модальном окне "Создать аккаунт" есть поле ввода Email
def test_placeholder_email(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR,"a.header__icon.header__icon_burger-mobile").click()
    placeholder_email = driver.find_element(By.CSS_SELECTOR, "input.form-type-text.js-pupop-global__field")
    assert placeholder_email.is_displayed, "Поле ввода email не найдено"
    print("Поле ввода email отображается на странице")


# в модальном окне "Создать аккаунт" есть поле ввода Пароль
def test_placeholder_password(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR,"a.header__icon.header__icon_burger-mobile").click()
    placeholder_password = driver.find_element(By.NAME, "REGISTER[PASSWORD]")
    assert placeholder_password.is_displayed, "Поле ввода Пароль не найдено"
    print("Поле ввода Пароль отображается на странице")


# в модальном окне "Создать аккаунт" есть поле ввода Подтверждение пароля
def test_placeholder_confirm_password(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR,"a.header__icon.header__icon_burger-mobile").click()
    placeholder_confirm_password = driver.find_element(By.NAME, "REGISTER[CONFIRM_PASSWORD]")
    assert placeholder_confirm_password.is_displayed, "Поле ввода Подтверждения пароля не найдено"
    print("Поле ввода Подтверждения пароля отображается на странице")


# "Политика конфиденциальности" есть на сайте
def test_google_privacy(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    google_privacy = driver.find_element(By.XPATH, "//div[@class='recaptcha-info']//a[@href='https://policies.google.com/privacy']")
    assert google_privacy.is_displayed, "Ссылка на 'Политика конфиденциальности' не найдена"
    print("Ссылка на 'Политика конфиденциальности' найдена")


# Тап по "политика конфиденциальности" открывает ссылку в новом окне
def test_google_privacy_doc(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    google_privacy_doc = driver.find_element(By.XPATH, "//div[@class='recaptcha-info']//a[@href='https://policies.google.com/privacy']")
    google_privacy_doc.click()
    assert google_privacy_doc.is_displayed, "Ссылка на 'Политика конфиденциальности' не найдена"
    print("Ссылка на 'Политика конфиденциальности' найдена")


# "Условия использования" Google есть на сайте
def test_google_terms(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    google_terms = driver.find_element(By.XPATH, "//div[@class='recaptcha-info']//a[@href='https://policies.google.com/terms']")
    assert google_terms.is_displayed, "Ссылка на 'Условия использования' не найдена"
    print("Ссылка на 'Условия использования' найдена")


# в модалке "Создать аккаунт" есть кнопка "Зарегистрироваться"
def test_button_reg_in(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    time.sleep(2)
    button_reg_in = driver.find_element(By.CSS_SELECTOR, "button.btn.js-popup-global__btn-registration")
    assert button_reg_in.is_displayed(), "Кнопка регистрации не видна"
    print("Кнопка регистрации найдена и видна")


# в модальном окне "Создать аккаунт" есть кнопка "Войти"
def test_button_login(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    time.sleep(2)
    button_login = driver.find_element(By.XPATH, "//span[text()='Войти']")
    assert button_login.is_displayed(), "Кнопка входа не видна"
    print("Кнопка входа найдена и видна")


# в модальном окне "Создать аккаунт" есть кнопка "Политика конфиденциальности"
def test_global_policy(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    time.sleep(2)
    button_global_policy = driver.find_element(By.CSS_SELECTOR, "a.popup-global__policy")
    assert button_global_policy.is_displayed(), "Кнопка Политика конфиденциальности не найдена"
    print("Кнопка Политика конфиденциальности найдена")


# в модальном окне "Создать аккаунт" есть кнопка-крестик
def test_button_modal_close(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    button_modal_close = driver.find_element(By.CSS_SELECTOR, "button.modal__close.js-close-modal")
    assert button_modal_close is not None, "Кнопка-крестик не найдена"
    driver.execute_script("arguments[0].click();", button_modal_close)
    print("Кнопка-крестик отображается в модалке")



"""________ АВТОРИЗАЦИЯ ________"""
# авторизация пользователя не пройдена (неверный пароль)
def test_authorization_fail(driver: WebDriver, sauce_site):
    driver.find_element(By.CSS_SELECTOR, "a.header__icon.header__icon_burger-mobile").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Войти']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "USER_LOGIN").send_keys('konfeti09@mail.ru')
    driver.find_element(By.NAME, "USER_PASSWORD").send_keys('WRONG_PASSWORD')
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(2)

    current_url = driver.current_url
    assert "personal/donations" not in current_url, f"Произошел переход, хотя данные неверные. URL: {current_url}"

    error_message = driver.find_element(By.XPATH, "//label[text()='Неверный логин или пароль']")
    assert error_message.is_displayed(), "Сообщение об ошибке не появилось"
    assert "Неверный логин или пароль" in error_message.text, "Текст ошибки не совпадает"

    print("Пользователь не авторизован")






