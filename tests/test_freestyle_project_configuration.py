import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser

FREESTYLE_PROJECT_NAME = "Freestyle Project"
SCM_TITLE_EXPECTED = "Source Code Management"


def wait_until_clickable(browser: WebDriver, locator: tuple[str, str], timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )

@pytest.mark.dependency()
def test_create_freestyle_project(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys('Test')
    browser.find_element(By.CSS_SELECTOR, "li.hudson_model_FreeStyleProject").click()
    browser.find_element(By.XPATH, '//*[@id="ok-button"]').click()
    browser.find_element(By.NAME, "Submit").click()

@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_disable_active_project(browser):
    wait = WebDriverWait(browser, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "main-panel")))
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.app-jenkins-logo"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.jenkins-menu-dropdown-chevron"))
    ).click()
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'configure')]"))
    )
    browser.find_element(By.XPATH, "//a[contains(@href, 'configure')]").click()

    browser.find_element(By.CSS_SELECTOR, 'label[for="enable-disable-project"]').click()
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(
        By.XPATH, "//*[contains(text(), 'This project is currently disabled')]"
    )


def test_access_scm_title(browser):
    browser.find_element(By.XPATH, "//a[@href='newJob']").click()

    browser.find_element(By.ID, "name").send_keys(FREESTYLE_PROJECT_NAME)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    wait_until_clickable(browser, (By.ID, "ok-button")).click()

    scm_title_text = wait_until_clickable(browser, (By.ID, "source-code-management")).text

    assert scm_title_text == SCM_TITLE_EXPECTED


@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_add_description_to_existing_freestyle_project(browser):
    wait = WebDriverWait(browser, 10)

    browser.find_element(By.ID, "description-link").click()
    browser.find_element(By.NAME, "description").send_keys("Test description")
    browser.find_element(By.NAME, "Submit").click()

    assert wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='description-content' and contains(., 'Test description')]")
    )
)
