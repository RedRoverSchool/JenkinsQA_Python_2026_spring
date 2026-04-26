from gc import enable

from requests import options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options # именно для Chrome
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-extensions")
options.add_argument("--lang=en-US")
service =  Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# browser = webdriver.Chrome(options=options)

# def test_title_check():
#     """Title check"""
#     driver.get("https://grok.com/")
#     assert "Grok" in driver.title
#
# def test_authr_link():
#     """Authorisation check"""
#     driver.get("https://grok.com/")
#     time.sleep(3)
#     login_button = driver.find_element(By.LINK_TEXT, "Sign in")
#     login_button.click()
#     time.sleep(2)
#     """В assert через запятую указывается ответ при падении теста"""
#     assert driver.current_url != "https://grok.com/", "Ошибка: URL не изменился, мы всё еще на главной!"

def test_container_authr():
    driver.get("https://grok.com/")
    time.sleep(2)
    login_button = driver.find_element(By.LINK_TEXT, "Sign in")
    login_button.click()
    time.sleep(2)
    auth_container = lambda text: (By.XPATH, f"//button[contains(., '{text}')]")
    login_email = driver.find_element(*auth_container("Login with email"))
    auth_google = driver.find_element(*auth_container("Login with Google"))
    auth_apple = driver.find_element(*auth_container("Login with Apple"))
    assert "Login with email" in login_email.text
    assert "Login with Google" in auth_google.text
    assert "Login with Apple" in auth_apple.text #ищут текст в элементе


# def test_placeholder_check():
#     driver.get("https://grok.com/")
#     time.sleep(10)
#     search = driver.find_element(By.CSS_SELECTOR, "textarea.w-full")
#     expected_variants = ["What's on your mind?", "What do you want to know?", "How can I help you today?"]
#     assert search.get_attribute("placeholder") in expected_variants
#
# def test_submit_search():
#     driver.get("https://grok.com/")
#     time.sleep(4)
#     search = driver.find_element(By.CSS_SELECTOR, "textarea.w-full")
#     search.clear()
#     search.send_keys("pytest selenium")
#     assert search.get_attribute("value") == "pytest selenium"

# def test_search_button():
#     browser.get("https://grok.com/")
#     search = browser.find_element(By.CSS_SELECTOR, "textarea.w-full")
#     search.clear()
#     search.send_keys("pytest selenium")