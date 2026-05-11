from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.project_page import ProjectPage


class FreestyleConfigPage(BasePage):
    def set_description(self, text):
        self.wait10.until(EC.visibility_of_element_located((By.NAME, "description"))).send_keys(text)

        return self

    def save(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return ProjectPage(self.driver)
