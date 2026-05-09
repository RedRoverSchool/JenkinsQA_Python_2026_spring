from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize("job_name, pipeline_description",[
    ("PipelineName1","my_first_pipeline"),
    ("PipelineName2", "my_second_pipeline"),
    ("PipelineName3", "my_third_pipeline")

])
@pytest.mark.dependency(name='test_create_several_pipelines')
def test_create_several_pipelines(browser, job_name, pipeline_description):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys(job_name)
    browser.find_element(By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob']").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    browser.find_element(By.XPATH, "(//textarea[@name='description'])[1]").send_keys(pipeline_description)
    browser.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    browser.find_element(By.XPATH, f"//span[normalize-space()='{job_name}']")
    browser.find_element(By.ID, "jenkins-head-icon").click()
    created_pipeline = browser.find_element(By.CSS_SELECTOR, ".jenkins-table__link >span:first-child").text

    assert created_pipeline == job_name


@pytest.mark.dependency(depends=["test_create_several_pipelines"])
def test_copy_from_existing_pipeline(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys("my_fourth_pipeline")
    browser.find_element(By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_job_WorkflowJob']").click()
    browser.find_element(By.XPATH, "(//input[@id='from'])[1]").send_keys("Pipe")
    browser.find_element(By.XPATH, "//a[normalize-space()='PipelineName3']").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    browser.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    actual_description = browser.find_element(By.XPATH, "//div[@id='description-content']").text
    assert actual_description == "my_third_pipeline"