import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FOLDER_NAME = "TestFolder"
DISPLAY_NAME = "Display Folder"

def create_folder(driver, name, full_creation=True):
    driver.find_element(By.XPATH, "//a[contains(@href, '/newJob')]").click()
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "ok-button"))
    ).click()
    if full_creation:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "Submit"))
        ).click()

@pytest.mark.dependency()
def test_add_display_name_to_folder(browser):
    create_folder(browser, FOLDER_NAME)
    browser.find_element(By.XPATH, "//a[contains(@href, '/configure')]").click()

    browser.find_element(By.NAME, "_.displayNameOrNull").send_keys(DISPLAY_NAME)
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == DISPLAY_NAME
    folder_name_line = \
        [line for line in browser.find_element(By.ID, "main-panel").text.split('\n') if
         line.startswith("Folder name: ")][0]
    assert folder_name_line == f"Folder name: {FOLDER_NAME}"
