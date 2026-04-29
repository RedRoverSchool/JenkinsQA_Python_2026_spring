import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_create_from_copy(browser):
    wait = WebDriverWait(browser, 10)

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "New Item"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="name"]'))
    ).send_keys('My first folder')

    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder'))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, 'ok-button'))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@value="Save"]'))
    ).click()
    time.sleep(2)

    wait.until(
        EC.element_to_be_clickable((By.ID, 'jenkins-head-icon'))
    ).click()

    browser.find_element(By.LINK_TEXT, "New Item").click()

    browser.find_element(By.ID, 'name').send_keys('Folder from copy')

    browser.find_element(By.ID, 'from').send_keys('My first folder')
    browser.find_element(By.ID, 'from').send_keys(Keys.ENTER)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@value="Save"]'))
    ).click()
    time.sleep(2)

    wait.until(
        EC.element_to_be_clickable((By.ID, 'jenkins-head-icon'))
    ).click()

    folder = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Folder from copy')))
    assert folder.is_displayed()
