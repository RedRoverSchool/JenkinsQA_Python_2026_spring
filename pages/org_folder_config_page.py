from selenium.webdriver.common.by import By

from pages.base_project_page import BaseProjectPage
from pages.org_folder_status_page import StatusOrgFolderPage


class ConfigOrgFolderPage(BaseProjectPage):

    def set_display_name(self, name):
        self.driver.find_element(By.NAME, "_.displayNameOrNull").send_keys(name)

        return self

    def set_description_name(self, name):
        self.driver.find_element(By.NAME, "_.description").send_keys(name)

        return self

    def click_save(self):
        self.driver.find_element(By.NAME, "Submit").click()
        return StatusOrgFolderPage(self.driver)