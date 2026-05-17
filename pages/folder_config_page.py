from selenium.webdriver.common.by import By

from pages.base_config_page import BaseConfigPage


class FolderConfigPage(BaseConfigPage):
    def set_display_name(self, display_name):
        self.driver.find_element(By.NAME, "_.displayNameOrNull").send_keys(display_name)

        return self

