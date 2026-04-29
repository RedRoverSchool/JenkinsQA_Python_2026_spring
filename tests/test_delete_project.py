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
JOB_TITLE = (By.XPATH, "//h1[@class='job-index-headline page-headline']")

@pytest.fixture
def click(browser):
    def clicking(element):
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element)).click()
    return clicking

@pytest.fixture
def fill(browser):
    def filling(element, text):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(element)).send_keys(text)
    return filling

@pytest.fixture
def check_visibility(browser):
    def checking(element):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(element))
    return checking

def generate_project_name():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))

def create_job(click, fill, check_visibility, current_project_name, item_type=PIPELINE_ITEM_TYPE):
    click(NEW_ITEM_BUTTON)

    fill(INPUT_NEW_ITEM_FIELD, current_project_name)
    click(PIPELINE_ITEM_TYPE)
    click((By.XPATH, "//button[@id='ok-button']"))

    click((By.XPATH, "//button[@name='Submit']"))

    check_visibility(JOB_TITLE)
    click(JENKINS_LOGO)
    check_visibility(JENKINS_LOGO)

@pytest.mark.skip
def test_delete_job(browser, click, fill, check_visibility):
    current_project_name = generate_project_name()

    create_job(click, fill, check_visibility, current_project_name)
    browser.get(browser.current_url + f"/job/{current_project_name}/")

    click((By.XPATH, "//a[contains(@data-title, 'Delete')]"))
    click((By.XPATH, "//button[@data-id='ok']"))

    browser.get(browser.current_url + f"/job/{current_project_name}/")

    assert "404" in browser.title or "Not Found" in browser.page_source

def test_cancel_delete_job(browser, click, fill, check_visibility):
    current_project_name = generate_project_name()

    create_job(click, fill, check_visibility, current_project_name)
    browser.get(browser.current_url + f"/job/{current_project_name}/")

    click((By.XPATH, "//a[contains(@data-title, 'Delete')]"))
    click((By.XPATH, "//button[@data-id='cancel']"))

    browser.refresh()
    check_visibility(JOB_TITLE)

    assert browser.find_element(*JOB_TITLE).text == current_project_name
