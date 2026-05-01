import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

random_name = "item" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))


def create_new_item(driver: WebDriver):
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, "//a[contains(@href, 'newJob')]").click()

    wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(random_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='label' and text()='Freestyle project']"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()


def test_freestyle_project_configuration(browser):
    wait = WebDriverWait(browser, 5)

    create_new_item(browser)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@id='general']")))
    browser.find_element(By.XPATH, "//label[@data-title='Disabled']").click()
    browser.find_element(By.NAME, "Submit").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, f"//h1[contains(text(), '{random_name}')]")))
    current_text = browser.find_element(By.XPATH, "//*[@id='enable-project']").text
    enable_button = browser.find_element(By.NAME, "Submit")

    assert "This project is currently disabled" in current_text
    assert enable_button.is_displayed()
