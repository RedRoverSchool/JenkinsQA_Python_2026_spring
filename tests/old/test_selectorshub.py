import time

from selenium.webdriver.common.by import By

def test_dummy_form(browser):
    user_email = "test1@gmail.com"
    password = "1234"
    company = 'test company'
    mobile_number = "89507981232"
    country = "Russia"

    browser.get("https://selectorshub.com/xpath-practice-page/")

    # Заполняем форму
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys(user_email)

    password_field = browser.find_element(By.ID, "pass")
    password_field.send_keys(password)

    company_field = browser.find_element(By.NAME, "company")
    company_field.send_keys(company)

    mobile_field = browser.find_element(By.NAME, "mobile number")
    mobile_field.send_keys(mobile_number)

    country_field= browser.find_element(By.XPATH, "//label[contains(text(), 'Country')]/input")
    country_field.send_keys(country)

    # Проверяем корректность значений
    assert email_field.get_attribute("value") == user_email
    assert password_field.get_attribute("value") == password
    assert company_field .get_attribute("value") == company
    assert mobile_field.get_attribute("value") == mobile_number
    assert country_field.get_attribute("value") == country

    # Отправляем форму
    submit_button = browser.find_element(By.XPATH, "//button[@value='Submit']")
    browser.execute_script("arguments[0].click();", submit_button) # понимаю, что можно без execute_script, но здесь перекрытие кнопки, потому это единственное решение, для обхода
