import selenium
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_available_types(browser):
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/view/all/newJob']"))).click()

    work_flow_job= wait.until(EC.visibility_of_element_located((By.XPATH,'//li[@class="org_jenkinsci_plugins_workflow_job_WorkflowJob"]')))
    assert work_flow_job.is_displayed()

    free_style_project = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="hudson_model_FreeStyleProject"]')))
    assert free_style_project.is_displayed()

    matrix_project = wait.until(EC.visibility_of_element_located((By.XPATH,  '//li[@class="hudson_matrix_MatrixProject"]')))
    assert matrix_project.is_displayed()

    folder = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="com_cloudbees_hudson_plugins_folder_Folder"]')))
    assert folder.is_displayed()

    multibranch_project = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@class="org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject"]')))
    assert multibranch_project.is_displayed()

    organization_folder = wait.until(EC.visibility_of_element_located((By.XPATH,'//li[@class="jenkins_branch_OrganizationFolder"]')))
    assert organization_folder.is_displayed()