from selenium.webdriver.common.by import By
import  time

def test_main_page_title_1(browser):
    browser.get("https://av.by/")
    main_page_title = "av.by — купить, продать авто в Беларуси. Автомобили с пробегом и новые."
    assert "av.by — купить, продать авто в Беларуси." in browser.title
    assert main_page_title == browser.title


def test_cars_link_target_url(browser):
    browser.get("https://av.by/")
    cars_link = browser.find_element(By.LINK_TEXT, "Объявления")
    cars_link.click()
    assert browser.current_url == "https://cars.av.by/"

def test_cars_page_h1_text(browser):
    cars_page_h1_text = browser.find_element(By.TAG_NAME, "h1").text
    assert cars_page_h1_text == "Объявления о продаже автомобилей с пробегом в Беларуси"


def test_return_to_main_by_logo(browser):
    browser.get("https://av.by/")
    browser.find_element(By.LINK_TEXT, "Объявления").click()

    browser.find_element(By.CSS_SELECTOR, "a.header__logo-wrap").click()
    assert browser.current_url == "https://av.by/"


def test_login_with_invalid_password(browser):
    browser.get("https://av.by/")
    browser.find_element(By.LINK_TEXT, "Войти").click()

    browser.find_element(By.XPATH, "//div[@aria-labelledby='по телефону']//input[@id='authPhone']").send_keys("298734567")
    time.sleep(2)

    browser.find_element(By.XPATH, "//div[@aria-labelledby='по телефону']//input[@id='passwordPhone']").send_keys("invalid_password")
    time.sleep(2)

    submit_button_by_phone = browser.find_element(By.XPATH, "//div[@aria-labelledby='по телефону']//button[@type='submit' and @class='button button--action']")
    submit_button_by_phone.click()
    time.sleep(2)

    assert browser.find_element(By.CSS_SELECTOR, "div.error-message").text == "Неверный телефон или пароль. Если забыли пароль, восстановите его"




