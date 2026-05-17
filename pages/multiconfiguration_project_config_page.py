from pages.base_config_page import BaseConfigPage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.multiconfiguration_project_page import MulticonfigurationProjectPage


class MulticonfigurationProjectConfigPage(BaseConfigPage):
    def click_save_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return MulticonfigurationProjectPage(self.driver)

    def click_enable_toggle(self):
        self.wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#toggle-switch-enable-disable-project > label"))).click()

        return self

    def get_text_toggle_tooltip(self):
        enabled_toggle = self.driver.find_element(By.ID, "toggle-switch-enable-disable-project")

        ActionChains(self.driver).move_to_element(enabled_toggle).perform()

        return self.wait10.until(EC.visibility_of_element_located((By.CLASS_NAME, "tippy-content"))).text
