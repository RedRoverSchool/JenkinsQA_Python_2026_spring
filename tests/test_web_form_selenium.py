import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


def test_web_form(browser):#Тест на то что есть на странице элемент Web Form
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(5)
    assert browser.find_element(By.XPATH,"//h1[text()='Web form']").is_displayed()
    browser.quit()

def test_current_page(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    assert browser.current_url == "https://www.selenium.dev/selenium/web-form.html"
    browser.quit()

def test_text_input(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    text = browser.find_element(By.XPATH,"//input[@name='my-text']")
    text.send_keys("Hello World")
    assert text.get_attribute("value") == "Hello World"
    browser.quit()


def test_password_input(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    password = browser.find_element(By.XPATH,"//input[@type='password']")
    password.send_keys("qwerty123")
    assert password.get_attribute("value") == "qwerty123"
    browser.quit()

def test_text_area_input(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    area_text = browser.find_element(By.XPATH,"//textarea[@name='my-textarea']")
    area_text.send_keys("My name is Ruslan")
    assert type(area_text.get_attribute("value")) == str
    browser.quit()


def test_dropdown_select(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    select = browser.find_element(By.XPATH,"//select[@name='my-select']")
    time.sleep(2)
    select.click()
    drop_down = browser.find_element(By.XPATH,"//option[@value='2']")
    drop_down.click()
    assert select.get_attribute("value") == "2"
    browser.quit()

def test_cities_select(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    select_city = browser.find_element(By.XPATH,"//input[@name='my-datalist']")
    select_city.click()
    select_city.send_keys("Paris")
    time.sleep(2)
    assert select_city.get_attribute("value") == "Paris"
    browser.quit()

def test_select_date(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    calendar = browser.find_element(By.XPATH,"//input[@name='my-date']")
    calendar.click()
    month_next = browser.find_element(By.XPATH,"//th[text()='»']")
    month_next.click()
    time.sleep(4)
    date = browser.find_element(By.XPATH,"//td[text()='13']")
    date.click()
    assert calendar.get_attribute("value") == "05/13/2026"

# def test_example_range(browser):
#     browser.get("https://www.selenium.dev/selenium/web/web-form.html")
#     exaple_range = browser.find_element(By.XPATH,"//input[@value='5']")
#     exaple_range.get_attribute
#     time.sleep(2)
#     assert exaple_range.get_attribute("value") == '8'
#     browser.quit()

def test_checked_checkbox(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    check_box = browser.find_element(By.XPATH,"//input[@id='my-check-1']")
    check_box.click()
    check_box.click()
    assert check_box.is_selected()
    browser.quit()


def test_submit(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    text = browser.find_element(By.XPATH, "//input[@name='my-text']")
    text.send_keys("Hello World")
    password = browser.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("qwerty123")
    area_text = browser.find_element(By.XPATH, "//textarea[@name='my-textarea']")
    area_text.send_keys("My name is Ruslan")

    submit = browser.find_element(By.XPATH,"//button[text()='Submit']")
    submit.click()
    reserved = browser.find_element(By.XPATH, "//p[text()='Received!']").text
    assert reserved == "Received!"
    browser.quit()