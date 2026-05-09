import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_delete_project import click, check_visibility, create_job, fill, generate_project_name

MULTIBRANCH_PIPELINE_ITEM_TYPE = (By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject']")
NEW_NAME_INPUT_FIELD = (By.XPATH, "//input[@class='jenkins-input validated  ']")
JENKINS_LOGO = (By.XPATH, "//span[@class='jenkins-mobile-hide']")

def create_multibranch_and_go__to_rename_page(browser, click, fill,check_visibility):
    current_project_name = generate_project_name()

    create_job(click, fill, check_visibility, current_project_name, MULTIBRANCH_PIPELINE_ITEM_TYPE)
    browser.get(browser.current_url + f"job/{current_project_name}/confirm-rename")
    check_visibility(JENKINS_LOGO)

    return current_project_name

def test_rename_by_empty_string(browser, click, fill,check_visibility):
    create_multibranch_and_go__to_rename_page(browser, click, fill, check_visibility)

    browser.find_element(*NEW_NAME_INPUT_FIELD).clear()
    click((By.XPATH, "//div[@id='main-panel']"))
    check_visibility(NEW_NAME_INPUT_FIELD)

    assert browser.find_element(By.XPATH, "//div[@class='error']").text == "No name is specified"

@pytest.mark.parametrize("invalid_character", ["!", "/", "\\", "?", "%", "*", ":", "|", "<", ">", "#"])
def test_rename_by_invalid_characters(browser, click, fill,check_visibility, invalid_character):
    create_multibranch_and_go__to_rename_page(browser, click, fill, check_visibility)

    browser.find_element(*NEW_NAME_INPUT_FIELD).clear()
    fill(NEW_NAME_INPUT_FIELD, invalid_character)
    click((By.XPATH, "//div[@id='main-panel']"))
    wait10 = WebDriverWait(browser, 10)
    res = wait10.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='error']"), f"‘{invalid_character}’ is an unsafe character"))

    assert res == True

def test_rename_by_same_name(browser, click, fill, check_visibility):
    current_project_name = create_multibranch_and_go__to_rename_page(browser, click, fill, check_visibility)

    browser.find_element(*NEW_NAME_INPUT_FIELD).clear()
    fill(NEW_NAME_INPUT_FIELD, current_project_name)
    click((By.XPATH, "//div[@id='main-panel']"))
    wait10 = WebDriverWait(browser, 10)
    res = wait10.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='warning']"), "The new name is the same as the current name."))

    assert res == True

def test_rename_by_valid_name(browser, click, fill, check_visibility):
    create_multibranch_and_go__to_rename_page(browser, click, fill, check_visibility)
    new_name = generate_project_name()

    browser.find_element(*NEW_NAME_INPUT_FIELD).clear()
    fill(NEW_NAME_INPUT_FIELD, new_name)
    click((By.XPATH, "//button[@name='Submit']"))

    check_visibility((By.XPATH, "//h1[@class='job-index-headline page-headline']"))

    assert browser.find_element(By.XPATH, "//h1[@class='job-index-headline page-headline']").text == new_name