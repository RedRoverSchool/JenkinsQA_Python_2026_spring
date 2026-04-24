from selenium.webdriver.common.by import By


def test_navigate_to_configure_system_page(browser):
    manage_jenkins_button = browser.find_element(By.ID, "root-action-ManageJenkinsAction")
    manage_jenkins_button.click()
    system_button = browser.find_element(By.XPATH, "//a[@href='configure']")
    system_button.click()

    assert browser.title == "System - Manage Jenkins - Jenkins", "Configure System page did not open"
