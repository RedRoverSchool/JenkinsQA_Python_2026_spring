
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_new_freestyle_project(browser):
    driver = browser
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()

    project_name = f"test_project_{int(time.time())}"
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(project_name)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Freestyle project')]"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()

    wait.until(EC.presence_of_element_located((By.NAME, "Submit"))).click()

    wait.until(EC.url_contains("configure"))
    driver.get(driver.current_url.replace("/configure", ""))

    header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    assert project_name in header.text




