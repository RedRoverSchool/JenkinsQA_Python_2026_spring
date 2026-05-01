from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from common.jenkins_utils import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.project_utils import get_url


def test_header_quick_change_theme(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(By.XPATH, "//*[contains(text(), 'Dark') or contains (text(), 'dark')]").click()

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme.lower() == "dark"


def test_header_change_theme_through_appearance_page(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(By.XPATH, "//div[contains(@class, 'jenkins-dropdown')]//*[normalize-space()='Appearance']").click()
    browser.find_element(By.XPATH, "//div[@class='app-theme-picker__item']//*[contains(text(),'Dark') or contains(text(), 'dark')]").click()
    browser.find_element(By.XPATH, "//*[@class='jenkins-button apply-button']").click()

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme.lower() == "dark"


def test_check_updated_theme_after_logout(browser):

    user_menu = browser.find_element(By.ID, "root-action-UserAction")
    ActionChains(browser).move_to_element(user_menu).perform()

    browser.find_element(By.XPATH, "//div[contains(@class, 'jenkins-dropdown')]//*[normalize-space()='Appearance']").click()
    browser.find_element(By.XPATH, "//div[@class='app-theme-picker__item']//*[contains(text(),'Dark') or contains(text(), 'dark')]").click()
    browser.find_element(By.XPATH, "//*[@class='jenkins-button apply-button']").click()
    browser.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()

    browser.get(get_url().rstrip("/") + "/logout")
    browser.get(get_url().rstrip("/") + "/login")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "j_username")))

    login(browser)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "root-action-UserAction")))

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")
    assert theme.lower() == "dark"




