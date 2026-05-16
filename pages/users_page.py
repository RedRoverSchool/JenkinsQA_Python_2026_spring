from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.create_user_page import CreateUserPage
from pages.user_page import UserPage


class UsersPage(BasePage):


    def click_create_user(self) -> CreateUserPage:
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='addUser']"))).click()

        return CreateUserPage(self.driver)

    def click_user_id(self, user_id: str) -> UserPage:
        table = self.wait10.until(EC.visibility_of_element_located((By.XPATH, "//table[@id='people']")))
        table.find_element(By.XPATH, f".//a[@href='user/{user_id.lower()}/'"
                                     f" and contains(@class, 'jenkins-button')]").click()
        self.wait10.until(EC.staleness_of(table))

        return UserPage(self.driver)

    def is_find_user_name(self, user_name) -> bool:
        try:
            self.wait10.until(EC.visibility_of_element_located((By.XPATH,f"//table[@id='people']//a[text()='{user_name}']")))
            return True
        except NoSuchElementException:
            return False