
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

pipeline_name = "Pipeline_Name"

def create_pipeline_project(browser, name):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(name)
    browser.find_element(By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    browser.execute_script("""
                var logo = document.querySelector('.jenkins-mobile-hide');
                if (logo) logo.click();
            """)

@pytest.mark.skip
def test_create_project(browser):
    create_pipeline_project(browser, pipeline_name)
    created_pipeline = browser.find_element(By.CSS_SELECTOR, ".jenkins-table__link >span:first-child").text

    assert created_pipeline == pipeline_name

@pytest.mark.parametrize("job_name",[
    "PipelineName1",
    "PipelineName2",
    "PipelineName3"
])

def test_check_several_tests(browser, job_name):
    create_pipeline_project(browser, job_name)
    created_pipeline = browser.find_element(By.CSS_SELECTOR, ".jenkins-table__link >span:first-child").text

    assert created_pipeline == job_name
