from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.freestyle_config_page import FreestyleConfigPage
from pages.project_page import ProjectPage


class NewItemPage(BasePage):
    def set_project_name(self, name):
        self.wait10.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(name)

        return self

    def select_freestyle_and_ok_click(self):
        self.driver.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
        self.driver.find_element(By.ID, "ok-button").click()

        return FreestyleConfigPage(self.driver)

    def enter_copy_from(self, name):
        self.wait10.until(EC.element_to_be_clickable((By.ID, 'from'))).send_keys(name)

        return self

    def click_from_dropdown(self):
        self.wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='copy']"))).click()

        return self

    def click_ok(self):
        self.wait10.until(EC.element_to_be_clickable((By.ID, 'ok-button'))).click()
        return self  # или FreestyleConfigPage(self.driver), если страница конфигурации отдельно

    def click_save(self):
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()
        return ProjectPage(self.driver)
