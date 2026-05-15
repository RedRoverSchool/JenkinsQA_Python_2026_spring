from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.create_user_page import CreateUserPage


class UsersPage(BasePage):

    def click_create_user(self):

        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='addUser']"))).click()

        return CreateUserPage(self.driver)

    def is_find_user_name(self, user_name) -> bool:
        try:
            self.wait10.until(EC.visibility_of_element_located((By.XPATH,f"//table[@id='people']//a[text()='{user_name}']")))
            return True
        except NoSuchElementException:
            return False