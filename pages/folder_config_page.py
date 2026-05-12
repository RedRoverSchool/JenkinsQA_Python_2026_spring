from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.folder_page import FolderPage
from pages.project_page import ProjectPage


class FolderConfigPage(BasePage):
    def save_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return FolderPage(self.driver)

    def set_display_name(self, display_name):
        self.driver.find_element(By.NAME, "_.displayNameOrNull").send_keys(display_name)

        return self

    def set_description(self, description):
        self.driver.find_element(By.NAME, "_.description").send_keys(description)

        return self
