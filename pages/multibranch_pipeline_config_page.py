from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.multibranch_pipeline_page import MultiBranchPipelinePage

class MultiBranchPipelineConfigPage(BasePage):

    def click_submit_button(self):
        self.wait5.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return MultiBranchPipelinePage(self.driver)
