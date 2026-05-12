from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.project_page import ProjectPage


class FolderPage(ProjectPage):
    def get_config_description(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "view-message"))).text
