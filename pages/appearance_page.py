from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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

    def select_checkbox_show_pipeline_stages_on_job_page(self):
        if not self.driver.find_element(By.XPATH, '//input[@name="_.showGraphOnJobPage"]').is_selected():
            self.driver.find_element(By.XPATH, '//input[@name="_.showGraphOnJobPage"]/parent::span').click()

        return self