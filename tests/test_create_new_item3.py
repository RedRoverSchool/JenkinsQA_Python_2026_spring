from selenium.webdriver.common.by import By

description = "My first pipeline"

def create_new_pipeline(driver):
    driver.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("my_first_pipeline")
    driver.find_element(By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob']").click()
    driver.find_element(By.XPATH, "//button[@id='ok-button']").click()
    driver.find_element(By.XPATH, "(//textarea[@name='description'])[1]").send_keys(description)
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()


def test_copy_from(browser):

    create_new_pipeline(browser)

    browser.find_element(By.XPATH, "//span[normalize-space()='my_first_pipeline']")
    browser.find_element(By.ID, "jenkins-head-icon").click()
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.XPATH, "//input[@id='name']").click()
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys("my_second_pipeline")
    browser.find_element(By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob']").click()
    browser.find_element(By.XPATH, "(//input[@id='from'])[1]").send_keys("my")
    browser.find_element (By.XPATH, "//a[normalize-space()='my_first_pipeline']").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    browser.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    browser.find_element(By.XPATH, "//span[normalize-space()='my_second_pipeline']")

    result = browser.find_element(By.XPATH, "//div[@id='description-content']").text
    assert result == description
