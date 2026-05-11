from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProjectPage(BasePage):
    def get_description(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "description-content"))).text

    def get_project_name(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".job-index-headline.page-headline"))
        ).text
