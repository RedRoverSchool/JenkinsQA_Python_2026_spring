from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.multiconfiguration_project_page import MulticonfigurationProjectPage


class MulticonfigurationProjectConfigPage(BasePage):

    def save_button_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return MulticonfigurationProjectPage(self.driver)