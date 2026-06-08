from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from pages.base_project_page import BaseProjectPage


class StatusOrgFolderPage(BaseProjectPage):

    def get_display_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.job-index-headline").text.strip()

    def get_description(self):
        return self.driver.find_element(By.ID, "view-message").text.strip()