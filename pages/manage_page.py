from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.appearance_page import AppearancePage
from pages.base_page import BasePage
from pages.credentials_page import CredentialsPage
from pages.tools_page import ToolsPage
from pages.users_page import UsersPage


class ManagePage(BasePage):

    def credentials_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//*[@href ='credentials']"))).click()

        return CredentialsPage(self.driver)

    def click_users(self) -> UsersPage:
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='securityRealm/']"))).click()

        return UsersPage(self.driver)

    def click_tools(self):
        self.wait10.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@href='configureTools']"
            ))
        ).click()

        return ToolsPage(self.driver)

    def click_appearance(self) -> AppearancePage:
        self.driver.find_element(By.XPATH, "//a[@href='appearance']").click()

        return AppearancePage(self.driver)

    def check_appearance_visibility(self):
        return self.driver.find_element(By.XPATH, "//a[@href='appearance']").is_displayed()

    def search_field(self, query: str):
        field = self.wait10.until(EC.visibility_of_element_located((By.ID, "settings-search-bar")))
        field.clear()
        field.send_keys(query)

        return self

    def get_result_items_containing(self, letter: str):
        xpath = (
            f'//*[contains(@class, "jenkins-search__results-container--visible")]'
           f'//a[contains(translate(., "{letter.upper()}", "{letter.lower()}"), "{letter}")]'
        )

        return self.driver.find_elements(By.XPATH, xpath)

    def get_exact_result_item_text(self, text: str):
        xpath = (
            f'//*[contains(@class, "jenkins-search__results-container--visible")]'
            f'//a[normalize-space()="{text}"]'
        )
        item = self.wait10.until(EC.visibility_of_element_located((By.XPATH, xpath)))

        return item.get_attribute("textContent").strip()

    def clear_field_keyboard(self):
        field = self.wait10.until(EC.visibility_of_element_located((By.ID, "settings-search-bar")))
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.BACK_SPACE)

        return self

    def clear_field_method(self):
        field = self.wait10.until(EC.element_to_be_clickable((By.ID, "settings-search-bar")))
        field.click()
        self.driver.execute_script("arguments[0].value = '';", field)

        return self

    def get_field_value(self):

        return self.wait10.until(EC.visibility_of_element_located((By.ID, "settings-search-bar"))).get_attribute("value")