from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import getenv
from common.jenkins_utils import logout
from pages.home_page import HomePage

LOGIN_PAGE_TITLE = "Sign in - Jenkins"


def test_sign_out(browser):
    login_page = (
        HomePage(browser)
        .show_dropdown_menu_from_profile_icon()
        .dropdown_menu_sign_out_click()
    )

    assert login_page.get_title() == LOGIN_PAGE_TITLE

    assert login_page.get_username_field() == ""
    assert login_page.get_password_field() == ""


def test_sign_in_with_valid_username_and_password(browser):
    logout(browser)
    username = getenv("JENKINS_USERNAME")
    password = getenv("JENKINS_PASSWORD")
    wait = WebDriverWait(browser, 5)

    browser.find_element(By.ID, "j_username").send_keys(username)
    browser.find_element(By.ID, "j_password").send_keys(password)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@name="Submit"]'))
    ).click()
    wait.until_not(EC.url_contains("login"))

    assert browser.title == "Dashboard - Jenkins"


def test_sign_in_error_message(browser):
    logout(browser)
    username = "not valid username"
    password = "any password"
    wait = WebDriverWait(browser, 5)

    browser.find_element(By.ID, "j_username").send_keys(username)
    browser.find_element(By.ID, "j_password").send_keys(password)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@name="Submit"]'))
    ).click()

    result = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="app-sign-in-register__error"]')
        )
    )
    assert result.text == "Invalid username or password"
