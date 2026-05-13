from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.multibranch_pipeline_rename_page import MultiBranchPipelineRenamePage

class MultiBranchPipelinePage(BasePage):

    def click_rename_button(self):
        self.wait5.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Rename']"))).click()

        return MultiBranchPipelineRenamePage(self.driver)

    def get_project_name(self):
        return self.wait5.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='job-index-headline page-headline']"))).text