from pages.base_config_page import BaseConfigPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FolderConfigPage(BaseConfigPage):
    def set_display_name(self, display_name):
        self.driver.find_element(By.NAME, "_.displayNameOrNull").send_keys(display_name)

        return self

    def click_apply(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        return self

    def click_save(self):
        return self.wait10.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Saved']"))).text