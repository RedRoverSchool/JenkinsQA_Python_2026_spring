from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.credentials_page import CredentialsPage
from pages.tools_page import ToolsPage


class ManagePage(BasePage):
    def credentials_click(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//*[@href ='credentials']"))).click()

        return CredentialsPage(self.driver)

    def tools_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[@href='configureTools']"
            ))
        ).click()

        return ToolsPage(self.driver)
