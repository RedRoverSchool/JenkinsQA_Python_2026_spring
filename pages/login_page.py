from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def get_username_field(self):
        return self.driver.find_element(By.ID, "j_username").get_attribute("value")

    def get_password_field(self):
        return self.driver.find_element(By.ID, "j_password").get_attribute("value")

    def get_title(self):
        return self.driver.title
