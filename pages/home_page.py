from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.manage_page import ManagePage
from pages.new_item_page import NewItemPage


class HomePage(BasePage):
    def new_item_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))
        ).click()

        return NewItemPage(self.driver)

    def manage_gear_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@href = '/manage']"))
        ).click()

        return ManagePage(self.driver)

    def get_project_names_list(self):
        project_elements = self.driver.find_elements(By.CLASS_NAME, "jenkins-table__link")
        project_names = [element.text for element in project_elements]

        return project_names

    def schedule_build_click(self, job_name: str):
        self.driver.find_element(By.XPATH, f"//tr/td[7]//a[@tooltip='Schedule a Build for {job_name}']").click()

        return self

    def get_names_jobs_list_build_queue(self) -> list:
        list_elements = self.driver.find_elements(By.XPATH,
                                                  f" //div[@class='pane-content']//tr/td/a[@class='model-link inside tl-tr']")
        return [name_job.text for name_job in list_elements]
