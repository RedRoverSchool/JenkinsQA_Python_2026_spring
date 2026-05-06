from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

FREESTYLE_PROJECT_NAME = "freestyle_project"
description = "Description Freestyle Project"


@pytest.mark.dependency()
def test_create_freestyle_project(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(FREESTYLE_PROJECT_NAME)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.XPATH, "//textarea[@name='description']").send_keys(description)
    browser.find_element(By.NAME, "Submit").click()
    assert browser.find_element(By.ID, "description-content").text == description

    assert browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text == FREESTYLE_PROJECT_NAME


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_rename_freestyle_project_page_from_dashboard(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'app-jenkins-logo'))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="job/{FREESTYLE_PROJECT_NAME}/"]>.jenkins-menu-dropdown-chevron'))).click()
    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Rename'))).click()

    rename_page_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
    assert rename_page_title == f'Rename Project {FREESTYLE_PROJECT_NAME}'