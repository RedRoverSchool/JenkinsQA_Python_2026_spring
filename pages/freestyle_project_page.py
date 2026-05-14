from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class FreestyleProjectPage(BasePage):

    def get_warning_message(self, random_name):
        self.wait10.until(EC.visibility_of_element_located((By.XPATH, f"//h1[contains(text(), '{random_name}')]")))
        current_text = self.driver.find_element(By.XPATH, "//*[@id='enable-project']").text

        return current_text


    def get_status_button(self):
        enable_button = self.driver.find_element(By.NAME, "Submit")

        return enable_button