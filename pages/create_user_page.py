import pages
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class CreateUserPage(BasePage):


    def set_input(self, element_key: str, value: str):
        """
        :param element_key: name поля в которое нужно вставить текст.
                            На странице имеются поля:
                            username, password1, password2, fullname, email.
        :param value: Текст вставляемый в поле.
        :return: CreateUserPage
        """
        self.driver.find_element(By.XPATH, f"//input[@name='{element_key}']").send_keys(value)

        return self

    def click_create_user(self):
        self.driver.find_element(By.XPATH, "//button[@name='Submit']").click()

        return pages.users_page.UsersPage(self.driver)
