from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "j_username")
    PASSWORD_FIELD = (By.ID, "j_password")
    SIGN_IN_BUTTON = (By.NAME, "Submit")
    ERROR_MESSAGE = (By.XPATH, '//div[@class="app-sign-in-register__error"]')

    def login(self, username, password):
        self.wait10.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.wait10.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()

        from pages.home_page import HomePage

        return HomePage(self.driver)

    def get_username_field(self):
        return self.wait10.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).get_attribute("value")

    def get_password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("value")

    def get_title(self):
        return self.driver.title

    def set_username_field(self, username):
        self.wait10.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD)
        ).send_keys(username)

        return self

    def set_password_field(self, password):
        self.wait10.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        ).send_keys(password)

        return self

    def sign_in_button_click(self):
        self.wait10.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()

        return self

    def get_error_message(self):
        return self.wait10.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text
