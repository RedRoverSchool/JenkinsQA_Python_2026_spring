from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.project_page import ProjectPage
from pages.base_page import BasePage


class MulticonfigurationProjectPage(ProjectPage):
    def get_disable_project_message(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "enable-project"))).text
