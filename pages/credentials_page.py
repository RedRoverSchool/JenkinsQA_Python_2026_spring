from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


from pages.base_page import BasePage


class CredentialsPage(BasePage):

    def cancel_delete(self):
        self.driver.find_element(By.XPATH, "//button[@data-id = 'cancel']").click()

        return self

    def click_add_credentials_button(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add Credentials')]").click()

        return self

    def click_add_in_privet_key(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

        return self

    def click_next_button(self):
        self.driver.find_element(By.ID, "cr-dialog-next").click()

        return self

    def click_submit_button(self):
        self.driver.find_element(By.ID, "cr-dialog-submit").click()
        self.wait10.until(EC.presence_of_element_located((By.XPATH, "//div[@id='notification-bar']")))

        return self

    def click_delete(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Delete credential')]").click()

        return self

    def confirm_delete(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-id = 'ok']"))
        ).click()

        return self

    def fill_credential_form(self, username, password, credential_id, description):
        self.driver.find_element(By.NAME, "_.username").send_keys(username)
        self.driver.find_element(By.NAME, "_.password").send_keys(password)
        self.driver.find_element(By.NAME, "_.id").send_keys(credential_id)
        self.driver.find_element(By.NAME, "_.description").send_keys(description)

        return self

    def find_credential_card(self, username=None, description=None, credential_id=None):
        if credential_id:
            locator = (
                By.XPATH,
                f"//*[@href='credential/{credential_id}']"
            )
        else:
            locator = (
                By.XPATH,
                f'//div[contains(@class, "credentials-card")]'
                f'[.//span[contains(text(),"{username}/******")]]'
                f'[.//span[contains(text(),"{description}")]]'
            )

        return self.driver.find_element(*locator)

    def get_credential_cards(self):

        return self.driver.find_elements(By.CSS_SELECTOR, ".credentials-card")

    def is_credential_present(self, credential_id=None, username=None, description=None):
        if credential_id:
            xpath = f"//a[contains(@href, '/credential/{credential_id}')]"
        else:
            xpath = '//div[contains(@class, "credentials-card")]'

            if username:
                xpath += f'[.//span[contains(text(),"{username}/******")]]'

            if description:
                xpath += f'[.//span[contains(text(),"{description}")]]'

        return bool(self.driver.find_elements(By.XPATH, xpath))

    def is_empty_message_visible(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.XPATH,"//div[contains(text(), 'This credentials domain is empty')]")
                                             )).is_displayed()

    def open_actions_menu(self):
        self.driver.find_element(By.XPATH, "//*[@title = 'More actions']").click()

        return self

    def select_checkbox_treat_username_as_secret(self):
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Treat username as secret']").click()

        return self

    def select_radiobutton_enter_directly(self):
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Enter directly']").click()

        return self

    def select_ssh_username_with_private_key(self):
        self.driver.find_element(By.XPATH, "//div[contains(text(),'SSH Username with private key')]").click()

        return self

    def select_system_in_add_ssh_username(self):
        Select(self.driver.find_element(By.NAME, '_.scope')).select_by_value('SYSTEM')

        return self

    def select_username_with_password_type(self):
        self.driver.find_element(By.XPATH, "//div[text() = 'Username with password']").click()

        return self

    def set_description(self, text_to_insert: str):
        self.driver.find_element(By.NAME, '_.description').send_keys(text_to_insert)

        return self

    def set_id(self, text_to_insert: str):
        self.driver.find_element(By.NAME, '_.id').send_keys(text_to_insert)

        return self

    def set_passphrase(self, text_to_insert: str):
        self.driver.find_element(By.NAME, '_.passphrase').send_keys(text_to_insert)

        return self

    def set_privet_key(self, text_to_insert: str):
        self.driver.find_element(By.NAME, '_.privateKey').send_keys(text_to_insert)

        return self

    def set_username(self, text_to_insert: str):
        self.driver.find_element(By.NAME, '_.username').send_keys("testUsername")

        return self
