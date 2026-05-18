from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ViewPage(BasePage):
    def delete_user_view(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-title='Delete View']"))).click()
        self.wait10.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-id='ok']"))).click()

        return self

    def get_view_panel_elements(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "tabBarFrame"))).text