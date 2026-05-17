from pages.base_project_page import BaseProjectPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MulticonfigurationProjectPage(BaseProjectPage):
    def get_disable_project_message(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "enable-project"))).text
