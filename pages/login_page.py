from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    def get_username_field(self):
        return self.driver.find_element(By.ID, "j_username").get_attribute("value")

    def get_password_field(self):
        return self.driver.find_element(By.ID, "j_password").get_attribute("value")

    def set_username_field(self, username):
        self.driver.find_element(By.ID, "j_username").send_keys(username)

        return self

    def set_password_field(self, password):
        self.driver.find_element(By.ID, "j_password").send_keys(password)

        return self

    def sign_in_with_valid_credentials_click(self):
        from pages.home_page import HomePage

        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@name="Submit"]'))
        ).click()
        self.wait10.until_not(EC.url_contains("login"))

        return HomePage(self.driver)
