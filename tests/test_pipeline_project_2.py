import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PIPELINE_NAME = "test_1"

@pytest.mark.dependency()
def test_create_pipeline_project(browser):
    wait = WebDriverWait(browser, 7)

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
    WebDriverWait(browser, 7).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Configure']"))).click()
    browser.find_element(By.NAME, "description").send_keys(text_description)
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(By.ID, "description-content").text == text_description

@pytest.mark.dependency(depends=["test_create_pipeline_project"])
def test_configure_display_name_by_advanced(browser):
    advanced_name = "Display Name"

    wait = WebDriverWait(browser, 7)
    browser.find_element(By.LINK_TEXT, PIPELINE_NAME).click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Configure']"))).click()

    advanced_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][normalize-space()='Advanced'])[3]")))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", advanced_button)
    browser.execute_script("arguments[0].click();", advanced_button)
    browser.find_element(By.XPATH, "//input[@name='_.displayNameOrNull']").send_keys(advanced_name)
    browser.find_element(By.NAME, "Submit").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Permalinks']")))
    browser.find_element(By.XPATH, "//*[@class='app-jenkins-logo']").click()

    wait.until(EC.visibility_of_element_located((By.ID, 'description-link')))
    display_name_element = browser.find_element(By.XPATH, "//span[text()='Display Name']").text

    assert display_name_element == advanced_name
