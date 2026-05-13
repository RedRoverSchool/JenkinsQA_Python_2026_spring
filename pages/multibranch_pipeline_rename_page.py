from email import message
from urllib import error

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MultiBranchPipelineRenamePage(BasePage):

    def fill_rename_field(self, new_name: str, invalid_char: str = ""):
        self.wait5.until(EC.visibility_of_element_located((By.XPATH, "//input[@checkdependson]"))).clear()
        self.driver.find_element(By.XPATH, "//input[@checkdependson]").send_keys(new_name + invalid_char)
        # Кликаем на тело страницы чтобы появилась надпись предупреждения о недопустимом символе
        self.driver.find_element(By.XPATH, "//div[@id='main-panel']").click()

        return self

    def get_warning_message(self, invalid_char: str = ""):
        self.wait5.until(EC.text_to_be_present_in_element((By.XPATH, f"//div[@class='error']"), f"‘{invalid_char}’ is an unsafe character"))

        return self.driver.find_element(By.XPATH, f"//div[@class='error']").text

    def get_same_name_warning_message(self):
        self.wait5.until(EC.text_to_be_present_in_element((By.XPATH, f"//div[@class='warning']"),"The new name is the same as the current name."))

        return self.driver.find_element(By.XPATH, f"//div[@class='warning']").text

    def get_empty_name_warning_message(self):
        self.wait5.until(EC.text_to_be_present_in_element((By.XPATH, f"//div[@class='error']"),"No name is specified"))

        return self.driver.find_element(By.XPATH, f"//div[@class='error']").text

    def click_rename_submit_button(self):
        from pages.multibranch_pipeline_page import MultiBranchPipelinePage
        self.driver.find_element(By.XPATH, "//button[@name='Submit']").click()

        return MultiBranchPipelinePage(self.driver)

