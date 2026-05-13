from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.freestyle_config_page import FreestyleConfigPage
from pages.folder_config_page import FolderConfigPage
from pages.multibranch_pipeline_config_page import MultiBranchPipelineConfigPage
from pages.pipeline_config_page import PipelineConfigPage

class NewItemPage(BasePage):
    def set_project_name(self, name):
        self.wait10.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(name)

        return self

    def select_freestyle_and_ok_click(self):
        self.driver.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
        self.driver.find_element(By.ID, "ok-button").click()

        return FreestyleConfigPage(self.driver)

    def select_folder_and_ok_click(self):
        self.driver.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
        self.driver.find_element(By.ID, "ok-button").click()

        return FolderConfigPage(self.driver)

    def select_pipeline_and_ok_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "((//ul[@class='j-item-options'])[1]//li)[1]"))).click()
        self.driver.find_element(By.ID, "ok-button").click()

        return PipelineConfigPage(self.driver)

    def select_multibranch_and_ok_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject']"))).click()
        self.driver.find_element(By.ID, "ok-button").click()

        return MultiBranchPipelineConfigPage(self.driver)

    def select_folder(self):
        self.driver.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()

        return self

    def get_unsafe_character_error_message(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "itemname-invalid"))).text
