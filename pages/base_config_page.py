from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.base_project_page import BaseProjectPage
from pages.folder_page import FolderPage
from pages.freestyle_project_page import FreestyleProjectPage


class BaseConfigPage(BasePage):
    def click_save(self, job_type="project"):
        button = self.driver.find_element(By.NAME, "Submit")
        button.click()
        self.wait10.until(EC.staleness_of(button))
        if job_type == "project":
            return BaseProjectPage(self.driver)
        elif job_type == "folder":
            return FolderPage(self.driver)
        elif job_type == "freestyle_project":
            return FreestyleProjectPage(self.driver)
        return None

    def set_description(self, description):
        self.driver.find_element(By.XPATH, "//textarea[contains(@name, 'description')]").send_keys(description)

        return self
