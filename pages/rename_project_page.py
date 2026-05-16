from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class RanameProjectPage(BasePage):
    def get_rename_project_page_title(self):
        return self.wait10.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text

    def clear_rename_field(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[checkdependson="newName"]'))
        ).clear()

        return self

    def set_new_project_name(self, new_name):
        self.driver.find_element(By.CSS_SELECTOR, '[checkdependson="newName"]').send_keys(new_name)

        return self

    def click_main_panel(self):
        self.driver.find_element(By.ID, 'main-panel').click()
        return self

    def get_rename_project_error_message(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error'))
        ).text
