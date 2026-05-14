from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "j_username")
    PASSWORD_FIELD = (By.ID, "j_password")
    SIGN_IN_BUTTON = (By.NAME, "Submit")

    def login(self, username, password):
        self.wait10.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.wait10.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()

        from pages.home_page import HomePage
        return HomePage(self.driver)

    def get_username_field(self):
        return self.wait10.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)).get_attribute("value")

    def get_password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("value")

    def get_title(self):
        return self.driver.title
