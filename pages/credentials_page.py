from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CredentialsPage(BasePage):
    def add_credentials_button_click(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add Credentials')]").click()

        return self

    def select_username_with_password_type(self):
        self.driver.find_element(By.XPATH, "//div[text() = 'Username with password']").click()

        return self

    def next_button_click(self):
        self.driver.find_element(By.ID, "cr-dialog-next").click()

        return self

    def fill_credential_form(self, username, password, credential_id, description):
        self.driver.find_element(By.NAME, "_.username").send_keys(username)
        self.driver.find_element(By.NAME, "_.password").send_keys(password)
        self.driver.find_element(By.NAME, "_.id").send_keys(credential_id)
        self.driver.find_element(By.NAME, "_.description").send_keys(description)

        return self

    def submit_button_click(self):
        self.driver.find_element(By.ID, "cr-dialog-submit").click()

        return self

    def open_actions_menu(self):
        self.driver.find_element(By.XPATH, "//*[@title = 'More actions']").click()

        return self

    def delete_click(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Delete credential')]").click()

        return self

    def cancel_delete(self):
        self.driver.find_element(By.XPATH, "//button[@data-id = 'cancel']").click()

        return self

    def confirm_delete(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-id = 'ok']"))
        ).click()

        return self

    def is_empty_message_visible(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.XPATH,"//div[contains(text(), 'This credentials domain is empty')]")
        )).is_displayed()


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
