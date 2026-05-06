import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_new_freestyle_project(driver):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()
    project_name = f"test_project_{int(time.time())}"
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(project_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Freestyle project')]"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.url_contains('configure'))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'app-jenkins-logo'))).click()
    return project_name

def test_rename_freestyle_project_from_project_page(browser):
    wait = WebDriverWait(browser, 5)
    project_name = create_new_freestyle_project(browser)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="job/{project_name}/"]'))).click()
    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Rename'))).click()
    rename_page_title = browser.find_element(By.TAG_NAME, 'h1')
    assert rename_page_title.text == f'Rename Project {project_name}'