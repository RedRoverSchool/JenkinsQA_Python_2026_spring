import selenium
import pytest
from selenium.webdriver.common.by import By

def test_available_types(browser):
    browser.get("http://localhost:8080/")
    browser.find_element(By.XPATH,"//a[@href='/view/all/newJob']").click()


    element_pipeline = browser.find_element(By.XPATH,'//li[@class="org_jenkinsci_plugins_workflow_job_WorkflowJob"]')
    is_enabled = element_pipeline.is_enabled()
    is_displayed= element_pipeline.is_displayed()
    print(f"Pipeline is enabled: {is_enabled}  and  is displayed : {is_displayed}")

    element_freestyle_project = browser.find_element(By.XPATH, '//li[@class="hudson_model_FreeStyleProject"]')
    is_enabled = element_freestyle_project.is_enabled()
    is_displayed = element_freestyle_project.is_displayed()
    print(f"FreeStyleProject are enabled: {is_enabled}  and  is displayed : {is_displayed}")

    element_matrix_project = browser.find_element(By.XPATH,  '//li[@class="hudson_matrix_MatrixProject"]')
    is_enabled = element_matrix_project.is_enabled()
    print(f"MatrixProject is enabled: {is_enabled} and  is displayed : {is_displayed}")

    element_folder = browser.find_element(By.XPATH, '//li[@class="com_cloudbees_hudson_plugins_folder_Folder"]')
    is_enabled = element_folder.is_enabled()
    print(f"Folder is enabled: {is_enabled}  and  is displayed : {is_displayed}")

    element_multibranch_project = browser.find_element(By.XPATH, '//li[@class="org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject"]')
    is_enabled = element_multibranch_project.is_enabled()
    print(f"MultiBranchProject is enabled: {is_enabled}  and  is displayed : {is_displayed}")

    element_organization_folder = browser.find_element(By.XPATH,'//li[@class="jenkins_branch_OrganizationFolder"]')
    is_enabled = element_organization_folder.is_enabled()
    print(f"OrganizationFolder is enabled: {is_enabled}  and  is displayed : {is_displayed}")