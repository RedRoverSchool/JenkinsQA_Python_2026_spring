from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.project_page import ProjectPage
from pages.freestyle_project_page import FreestyleProjectPage


class FreestyleConfigPage(BasePage):
    def set_description(self, text):
        self.wait10.until(EC.visibility_of_element_located((By.NAME, "description"))).send_keys(text)

        return self

    def button_save_click(self):
        button = self.driver.find_element(By.NAME, "Submit")
        button.click()
        self.wait10.until(EC.staleness_of(button))

        return ProjectPage(self.driver)

    def button_save_click_2(self):
        button = self.driver.find_element(By.NAME, "Submit")
        button.click()
        self.wait10.until(EC.staleness_of(button))

        return FreestyleProjectPage(self.driver)

    def button_add_build_step_click(self):
        button_add_build_step = self.driver.find_element(By.XPATH, "//button[text()='Add build step']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button_add_build_step)
        button_add_build_step.click()
        self.wait10.until(EC.visibility_of_element_located((By.CLASS_NAME, "jenkins-dropdown__item")))

        return self

    def select_execute_shell_option(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Execute shell']").click()

        return self

    def set_shell_script(self, command_shell):
        (ActionChains(self.driver)
         .move_to_element(self.driver.find_element(By.XPATH, "//div[contains(@class, 'cm-s-default')]"))
         .click().send_keys(command_shell).perform())

        return self


    def click_enable_disable_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//label[@data-title='Disabled']"))).click()

        return self

    def enable_delete_workspace_before_build_starts(self):
        checkbox_label = self.wait5.until(EC.element_to_be_clickable((By.XPATH,"//label[contains(.,'Delete workspace before build starts')]")))

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",checkbox_label)
        checkbox_label.click()

        return self

    def click_save(self):
        self.driver.find_element(By.NAME, "Submit").click()
        from pages.freestyle_project_page import FreestyleProjectPage
        # Импорт внутри метода чтобы избежать ошибки ImportError due to a circular import

        return FreestyleProjectPage(self.driver)

    def is_delete_workspace_before_build_starts_selected(self):
        return (self.wait5.until(EC.presence_of_element_located((By.NAME, "hudson-plugins-ws_cleanup-PreBuildCleanup"))).
                is_selected())
