from selenium.webdriver.common.by import By

def test_create_disabled_pipeline(browser):
    browser.find_element(By.LINK_TEXT, "New Item").click()

    browser.find_element(By.ID, "name").send_keys("Disabled Pipeline")
    browser.find_element(By.CSS_SELECTOR, ".org_jenkinsci_plugins_workflow_job_WorkflowJob").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.CSS_SELECTOR, ".jenkins-toggle-switch__label").click()
    browser.find_element(By.NAME, "Submit").click()

    status_message = browser.find_element(By.ID, "enable-project").text
    assert "This project is currently disabled" in status_message
    assert browser.find_element(By.NAME, "Submit").is_displayed()

    browser.find_element(By.CSS_SELECTOR, "a[href='/']").click()

    project_status_icon = browser.find_element(By.XPATH, "(//*[name()='svg'][@title='Disabled'])[1]")

    assert project_status_icon.is_displayed()