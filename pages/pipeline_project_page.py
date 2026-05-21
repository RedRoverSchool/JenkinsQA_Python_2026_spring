from selenium.webdriver.common.by import By

from pages.base_project_page import BaseProjectPage


class PipelineProjectPage(BaseProjectPage):

    def is_display_stages(self) -> bool:
        return self.driver.find_element(By.XPATH, "//a[@href='multi-pipeline-graph']").is_displayed()