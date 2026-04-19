import time
from selenium.webdriver.common.by import By

# import time - встроенный модуль Python → работа со временем
# By - из библиотеки Selenium →  это способ сказать "Как найти эл-т на странице"


def test_main_page_h1_text(browser):
    browser.get("https://the-internet.herokuapp.com/")
    heading1 = browser.find_element(By.CSS_SELECTOR, ".heading")

    assert heading1.text == "Welcome to the-internet", "Неверный заголовок страницы"


def test_main_page_h2_text(browser):
    browser.get("https://the-internet.herokuapp.com/")
    heading2 = browser.find_element(By.TAG_NAME, "h2")

    assert heading2.text == "Available Examples", "Неверный подзаголовок страницы"


def test_main_page_link1(browser):
    browser.get("https://the-internet.herokuapp.com/")
    link1 = browser.find_element(By.LINK_TEXT, "A/B Testing")
    '''
    Другие варианты поиска этой линки из списка: 
    (By.CSS_SELECTOR, "ul li a") - возвращает ПЕРВЫЙ найденный элемент, который подходит под локатор
    (By.CSS_SELECTOR, "a[href='/abtest']"
    '''
    link1.click()

    time.sleep(2)

    assert browser.current_url == "https://the-internet.herokuapp.com/abtest", "Неверный url для /abtest"









