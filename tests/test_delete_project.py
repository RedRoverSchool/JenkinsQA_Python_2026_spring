import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

JENKINS_LOGO = (By.XPATH, "//span[@class='jenkins-mobile-hide']")
NEW_ITEM_BUTTON = (By.XPATH, "//a[@it]")
INPUT_NEW_ITEM_FIELD = (By.XPATH, "//input[@id='name']")
PIPELINE_ITEM_TYPE = (By.XPATH, "((//ul[@class='j-item-options'])[1]//li)[1]")
OK_BUTTON = (By.XPATH, "//button[@id='ok-button']")
SUBMIT_BUTTON = (By.XPATH, "//button[@name='Submit']")
JOB_TITLE = (By.XPATH, "//h1[@class='job-index-headline page-headline']")
DELETE_JOB = (By.XPATH, "//a[contains(@data-title, 'Delete')]")
NOT_FOUND_JOB_TITLE = (By.XPATH, "//h2[text()='Not Found']")
CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[@data-id='ok']")
CANCEL_DELETE_BUTTON = (By.XPATH, "//button[@data-id='cancel']")

@pytest.fixture
def click(browser):
    def clicking(element, duration):
        WebDriverWait(browser, duration).until(EC.element_to_be_clickable(element)).click()
    return clicking

@pytest.fixture
def fill(browser):
    def filling(element, text, duration):
        WebDriverWait(browser, duration).until(EC.visibility_of_element_located(element)).send_keys(text)
    return filling

@pytest.fixture
def check_visibility(browser):
    def checking(element, duration):
        WebDriverWait(browser, duration).until(EC.visibility_of_element_located(element))
    return checking

def generate_project_name():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))

def create_job(click, fill, check_visibility, current_project_name):

    click(NEW_ITEM_BUTTON, 5)

    fill(INPUT_NEW_ITEM_FIELD, current_project_name, 5)
    click(PIPELINE_ITEM_TYPE, 5)
    click(OK_BUTTON, 5)

    click(SUBMIT_BUTTON, 5)

    check_visibility(JOB_TITLE, 5)
    click(JENKINS_LOGO, 5)
    check_visibility(JENKINS_LOGO, 5)

def test_delete_job(browser, click, fill, check_visibility):

    current_project_name = generate_project_name()

    create_job(click, fill, check_visibility, current_project_name)
    browser.get(browser.current_url + f"/job/{current_project_name}/")

    click(DELETE_JOB, 5)
    click(CONFIRM_DELETE_BUTTON, 5)

    browser.get(browser.current_url + f"/job/{current_project_name}/")
    check_visibility(NOT_FOUND_JOB_TITLE, 5)

    assert browser.find_element(*NOT_FOUND_JOB_TITLE).text == "Not Found"

@pytest.mark.skip
def test_cancel_delete_job(browser, click, fill, check_visibility):

    current_project_name = generate_project_name()

    create_job(click, fill, check_visibility, current_project_name)
    browser.get(browser.current_url + f"/job/{current_project_name}/")

    click(DELETE_JOB, 5)
    click(CANCEL_DELETE_BUTTON, 5)

    browser.refresh()
    check_visibility(JOB_TITLE, 5)

    assert browser.find_element(*JOB_TITLE).text == current_project_name
