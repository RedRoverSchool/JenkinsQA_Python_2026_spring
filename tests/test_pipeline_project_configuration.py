import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PIPELINE_NAME = "test_1"

@pytest.mark.dependency()
def test_create_pipeline_project(browser):
    wait = WebDriverWait(browser, 5)

    browser.find_element(By.LINK_TEXT, "New Item").click()
    browser.find_element(By.ID, "name").send_keys(PIPELINE_NAME)
    browser.find_element(By.XPATH, "//ul/li//span[text()='Pipeline']").click()
    browser.find_element(By.ID, "ok-button").click()
    wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Permalinks']")))
    browser.find_element(By.XPATH, "//*[@class='app-jenkins-logo']").click()

    label = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@href='job/test_1/']"))).text
    assert label == PIPELINE_NAME


@pytest.mark.dependency(depends=["test_create_pipeline_project"])
def test_add_description_pipeline(browser):
    text_description = "Description here"

    browser.find_element(By.LINK_TEXT, PIPELINE_NAME).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Configure']"))).click()

    browser.find_element(By.NAME, "description").send_keys(text_description)
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(By.ID, "description-content").text == text_description


@pytest.mark.dependency(depends=["test_create_pipeline_project"])
def test_disable_pipeline(browser):
    wait = WebDriverWait(browser, 5)

    project_link = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@href='job/{PIPELINE_NAME}/']")))
    project_link.click()

    configure_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Configure']")))
    configure_link.click()

    toggle = wait.until(EC.element_to_be_clickable((By.ID, "toggle-switch-enable-disable-project")))
    toggle.click()

    browser.find_element(By.NAME, "Submit").click()

    warning_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'This project is currently disabled')]"))
)

    assert warning_message.is_displayed(), "Сообщение об откл. не отображается"
