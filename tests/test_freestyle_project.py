from selenium.webdriver.common.by import By

FREESTYLE_PROJECT_NAME = "Freestyle Project"
description = "Description Freestyle Project"


def test_create_freestyle_project(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(FREESTYLE_PROJECT_NAME)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.XPATH, "//textarea[@name='description']").send_keys(description)
    browser.find_element(By.NAME, "Submit").click()
    assert browser.find_element(By.ID, "description-content").text == description

    assert browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text == FREESTYLE_PROJECT_NAME
