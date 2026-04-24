import random
import string
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.skip()
def test_copy_from_text_field(browser):
    """TC_01.003.01. Verifies 'Copy from' Text Field available"""
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys("my_first_pipeline")
    browser.find_element(By.XPATH, "(//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob'])[1]").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    browser.find_element(By.XPATH, "(//textarea[@name='description'])[1]").send_keys("My first pipeline")
    browser.maximize_window()
    browser.execute_script("window.scrollBy({ top: 1200, left: 0, behavior: 'auto' });")
    sleep(1)
    browser.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
    browser.find_element(By.XPATH, "(//a[@class='app-jenkins-logo'])[1]").click()
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.execute_script("window.scrollBy({ top: 800, left: 0, behavior: 'auto' });")
    sleep(1)
    text_field = browser.find_element(By.XPATH, "(//label[normalize-space()='Copy from'])[1]")
    browser.find_element(By.XPATH, "(//input[@id='from'])[1]").click()
    browser.find_element(By.XPATH, "(//input[@id='from'])[1]").send_keys("my_first_pipeline")

    assert text_field.text == "Copy from"


def test_copy_form(browser):
    FIRST_NAME = "first_folder"
    random_name = "folder_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    wait = WebDriverWait(browser, 5)

    browser.find_element(By.XPATH, "//div[@id='tasks']//a[contains(@href, 'newJob')]").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='add-item-panel']//h1")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(FIRST_NAME)
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           "//div[@id='j-add-item-type-nested-projects']//li[contains(@class, 'com_cloudbees_hudson_plugins_folder_Folder')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ok-button']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='Submit']"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='tasks']")))

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='tasks']//a[contains(@href, 'newJob')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))).send_keys(random_name)
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                           "//div[@id='j-add-item-type-nested-projects']//li[contains(@class, 'com_cloudbees_hudson_plugins_folder_Folder')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='from']"))).send_keys(FIRST_NAME)

    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='tasks']")))

    copied_folder = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//a[@href='job/{random_name}/']")
    ))
    assert copied_folder.is_displayed(), f"Folder '{random_name}' was not copied successfully"
