from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_project_page import BaseProjectPage


class FreestyleProjectPage(BaseProjectPage):

    def get_warning_message(self, random_name):
        self.wait10.until(EC.visibility_of_element_located((By.XPATH, f"//h1[contains(text(), '{random_name}')]")))
        current_text = self.driver.find_element(By.XPATH, "//*[@id='enable-project']").text

        return current_text


    def get_status_button(self):
        enable_button = self.driver.find_element(By.NAME, "Submit")

        return enable_button

    def click_configure(self):
        from pages.freestyle_config_page import FreestyleConfigPage
        # Импорт внутри метода чтобы избежать ошибки ImportError due to a circular import
        self.driver.find_element(By.XPATH, "//a[contains(., 'Configure')]").click()

        return FreestyleConfigPage(self.driver)
    def click_enable_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='Submit'][value='Enable']"))).click()

        return self
