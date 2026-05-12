from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.project_page import ProjectPage


class FolderConfigPage(BasePage):
    def save_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return ProjectPage(self.driver)
