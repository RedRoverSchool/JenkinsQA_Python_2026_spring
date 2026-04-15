from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options # Импортируем именно для Chrome

options = Options()

# Принудительный выбор языка интерфейса(Автоматически сайты запрашиваются на русском:()
options.add_argument("--lang=en-US")

browser = webdriver.Chrome(options=options)

def test_title_check():
    """Title check"""
    browser.get("https://grok.com/")
    assert "Grok" in browser.title

def test_authr_link():
    """Authorisation check"""
    browser.get("https://grok.com/")
    time.sleep(3)
    login_button = browser.find_element(By.LINK_TEXT, "Sign in")
    login_button.click()
    time.sleep(2)
    """В assert через запятую указывается ответ при падении теста"""
    assert browser.current_url != "https://grok.com/", "Ошибка: URL не изменился, мы всё еще на главной!"

def test_container_authr():
    browser.get("https://grok.com/")
    time.sleep(2)
    login_button = browser.find_element(By.LINK_TEXT, "Sign in")
    login_button.click()
    time.sleep(2)
    """скопировал все классы полностью. разделяются точкой. запрос ищет элемент со всеми классами включительно"""
    auth_container = browser.find_element(By.CSS_SELECTOR, ".mx-auto.flex.w-full.flex-col.gap-6.max-w-sm")
    assert "Login with email" in auth_container.text
    assert "Login with Google" in auth_container.text
    assert "Login with Apple" in auth_container.text #ищут текст в элементе

def test_placeholder_check():
    browser.get("https://grok.com/")
    time.sleep(10)
    search = browser.find_element(By.CSS_SELECTOR, "textarea.w-full")
    expected_variants = ["What's on your mind?", "What do you want to know?", "How can I help you today?"]
    assert search.get_attribute("placeholder") in expected_variants

def test_submit_search():
    browser.get("https://grok.com/")
    time.sleep(4)
    search = browser.find_element(By.CSS_SELECTOR, "textarea.w-full")
    search.clear()
    search.send_keys("pytest selenium")
    assert search.get_attribute("value") == "pytest selenium"

# def test_search_button():
#     browser.get("https://grok.com/")
#     search = browser.find_element(By.CSS_SELECTOR, "textarea.w-full")
#     search.clear()
#     search.send_keys("pytest selenium")




