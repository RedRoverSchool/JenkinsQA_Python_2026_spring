from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_config_page import BaseConfigPage


class FreestyleConfigPage(BaseConfigPage):
    def button_add_build_step_click(self):
        button_add_build_step = self.driver.find_element(By.XPATH, "//button[text()='Add build step']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button_add_build_step)
        button_add_build_step.click()
        self.wait10.until(EC.visibility_of_element_located((By.CLASS_NAME, "jenkins-dropdown__item")))

        return self

    def select_execute_shell_option(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Execute shell']").click()

        return self

    def select_execute_option(self, option):
        self.driver.find_element(By.XPATH, f"//button[normalize-space()='{option}']").click()

        return self

    def set_shell_script(self, command, xpath="//div[contains(@class, 'cm-s-default')]"):
        (ActionChains(self.driver)
         .move_to_element(self.driver.find_element(By.XPATH, xpath))
         .click().send_keys(command).perform())

        return self

    def click_enable_disable_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//label[@data-title='Disabled']"))).click()

        return self


