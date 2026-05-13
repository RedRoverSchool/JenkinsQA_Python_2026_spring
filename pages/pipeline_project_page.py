from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PipelineProjectPage(BasePage):

    def get_project_name(self):
        return self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//h1[@class='job-index-headline page-headline']"))).text

    def click_delete_pipeline(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-title, 'Delete')]"))).click()

        return self

    def click_cancel_delete_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='cancel']"))).click()

        return self

    def refresh_pipeline_project_page(self):
        self.driver.refresh()

        return self

    def click_confirm_delete_button(self):
        from pages.home_page import HomePage
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='ok']"))).click()

        return HomePage(self.driver)