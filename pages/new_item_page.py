from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.freestyle_config_page import FreestyleConfigPage
from pages.pipeline_config_page import PipelineConfigPage


class NewItemPage(BasePage):
    def set_project_name(self, name):
        self.wait10.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(name)

        return self

    def select_freestyle_and_ok_click(self):
        self.driver.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
        self.driver.find_element(By.ID, "ok-button").click()

        return FreestyleConfigPage(self.driver)

    def select_pipeline_and_ok_click(self):
        self.driver.find_element(By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob").click()
        self.driver.find_element(By.ID, "ok-button").click()

        return PipelineConfigPage(self.driver)