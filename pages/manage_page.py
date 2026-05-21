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
