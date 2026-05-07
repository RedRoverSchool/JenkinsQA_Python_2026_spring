import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_pipeline_project(browser):
    test="test_1"
    wait = WebDriverWait(browser, 10)

    browser.find_element(By.LINK_TEXT, "New Item").click()
    browser.find_element(By.ID, "name").send_keys(test)

    browser.find_element(By.XPATH,"//ul/li//span[text()='Pipeline']").click()
    browser.find_element(By.ID, "ok-button").click()

    wait.until(EC.element_to_be_clickable((By.NAME,"Submit"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Permalinks']")))
    browser.find_element(By.XPATH, "//*[@class='app-jenkins-logo']").click()

    label=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@href='job/test_1/']"))).text
    assert label == test

