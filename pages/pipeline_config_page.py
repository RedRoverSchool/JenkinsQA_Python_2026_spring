from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.pipeline_project_page import PipelineProjectPage

class PipelineConfigPage(BasePage):

    def click_submit_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return PipelineProjectPage(self.driver)