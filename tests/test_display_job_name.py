import pytest
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_new_item_name(browser):
    random_name = "folder_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    return random_name

def create_new_pipeline(browser):

    pipeline_name = create_new_item_name(browser)

    wait = WebDriverWait(browser, 5)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@it]"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))).send_keys(pipeline_name)
    browser.find_element(By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob']").click()
    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()

    wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='jenkins-header__main']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@id='jenkins-head-icon']"))).click()

    new_job = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='jenkins-table__link model-link inside']")))

    return new_job.text

def test_display_pipeline_name(browser):

    new_pipeline = create_new_pipeline(browser)

    wait = WebDriverWait(browser, 5)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@it]"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='from']"))).send_keys(new_pipeline)
    dropdown_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='jenkins-dropdown__item ']")))
    dropdown_name = dropdown_list.text

    assert new_pipeline == dropdown_name