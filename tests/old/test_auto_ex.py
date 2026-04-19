from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def accept_cookies(browser):
    try:
        cookie_button = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[@aria-label='Consent' or .//p[contains(., 'Consent')] or .//p[contains(., 'Accept')] or .//p[contains(., 'Got it')]]"
            ))
        )
        cookie_button.click()
    except Exception:
        pass

def test_login_signup_title(browser):

    browser.get("https://automationexercise.com/")
    browser.implicitly_wait(1)
    accept_cookies(browser)
    signup_login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a"))
    )
    signup_login_button.click()
    login_title = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[1]/div/h2")
    signup_title = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/h2")


    assert login_title.text == "Login to your account"
    assert signup_title.text == "New User Signup!"


    browser.quit()

def test_signup_first(browser):
    browser.get("https://automationexercise.com/")
    browser.implicitly_wait(1)
    accept_cookies(browser)
    signup_login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a"))
    )
    signup_login_button.click()
    signup_name_input = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/form/input[2]")
    signup_email_input = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/form/input[3]")
    signup_button = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div[3]/div/form/button")

    signup_name_input.send_keys("John")
    signup_email_input.send_keys("john77123wick@gmail.com")
    signup_button.click()

    signup_account_information = browser.find_element(by=By.XPATH, value="/html/body/section/div/div/div/div[1]/h2/b")
    assert signup_account_information.text == "ENTER ACCOUNT INFORMATION"




