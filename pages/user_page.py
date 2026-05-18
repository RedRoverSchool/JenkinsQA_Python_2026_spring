from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserPage(BasePage):


    def get_user_name(self) -> str:
        return self.driver.find_element(By.XPATH, "//h1").text
