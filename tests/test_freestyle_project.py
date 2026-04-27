from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FREESTYLE_PROJECT_NAME = "Freestyle Project"
description = "Description Freestyle Project"
SCM_TITLE_EXPECTED = "Source Code Management"


def wait_until_clickable(browser, locator: tuple, timeout=10):
    """Ожидает кликабельности элемента и возвращает его."""
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def test_create_freestyle_project(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(FREESTYLE_PROJECT_NAME)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.XPATH, "//textarea[@name='description']").send_keys(description)
    browser.find_element(By.NAME, "Submit").click()
    assert browser.find_element(By.ID, "description-content").text == description

    assert browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text == FREESTYLE_PROJECT_NAME


def test_access_scm_title(browser):
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FREESTYLE_PROJECT_NAME)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    wait_until_clickable(browser, (By.ID, "ok-button")).click()

    scm_title_text = wait_until_clickable(browser, (By.ID, "source-code-management")).text

    assert scm_title_text == SCM_TITLE_EXPECTED
