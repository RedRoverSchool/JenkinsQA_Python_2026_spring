import time
from selenium.webdriver.common.by import By

def test_new_job(browser):
    job_create = browser.find_element(By.XPATH, "//*[@href='newJob']")
    job_create.click()

    time.sleep(1)

    field_input = browser.find_element(By.XPATH, "//*[@id='name']")
    field_input.send_keys("test_job")

    time.sleep(1)

    freestyle_project_item = browser.find_element(By.XPATH, "//*[@role='radio']")
    freestyle_project_item.click()

    submit_button = browser.find_element(By.XPATH, "//*[@id='ok-button']")
    submit_button.click()

    time.sleep(1)

    home_page_logo = browser.find_element(By.XPATH, "//*[@class='app-jenkins-logo']")
    home_page_logo.click()

    time.sleep(1)

    item_name = browser.find_element(By.XPATH, "//*[@href='job/test_job/']")
    assert item_name.text == "test_job"



