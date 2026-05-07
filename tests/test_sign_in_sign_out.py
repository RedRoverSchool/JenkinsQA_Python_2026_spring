import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from common.jenkins_utils import logout

@pytest.mark.dependency()
def test_sign_in(browser):
    logout(browser)

    load_dotenv()
    username = os.getenv("JENKINS_USERNAME")
    password = os.getenv("JENKINS_PASSWORD")

    wait = WebDriverWait(browser, 10)

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "j_username"))).send_keys(username)
    password_field = browser.find_element(By.ID, "j_password").send_keys(password)

    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main-panel > div > form > button"))).click()

    jenkins_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#jenkins-head-icon")))

    assert jenkins_icon.is_displayed()

@pytest.mark.dependency(depends=["test_sign_in"])
def test_sign_out(browser):
    wait = WebDriverWait(browser, 10)

    user_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root-action-UserAction")))
    actions = ActionChains(browser)
    actions.move_to_element(user_icon).perform()

    sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/logout')]")))
    try:
        sign_out_button.click()
    except StaleElementReferenceException:
        sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/logout')]"))).click()

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "j_username")))
    password_field = browser.find_element(By.ID, "j_password")

    assert username_field.get_attribute("value") == ""
    assert password_field.get_attribute("value") == ""






