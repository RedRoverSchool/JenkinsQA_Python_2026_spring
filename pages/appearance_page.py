from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import pages


class AppearancePage(BasePage):

    def set_theme(self, theme):
        """
        :param theme: принимает `none`,`dark`,`dark-system`
        """
        self.driver.find_element(By.XPATH, f"//div[@data-theme='{theme}']/parent::label").click()

        return self

    def click_apply_button(self):
        self.driver.find_element(By.XPATH, "//button[@name='Apply']").click()

        return self