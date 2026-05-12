from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.new_item_page import NewItemPage


class HomePage(BasePage):
    def new_item_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))
        ).click()

        return NewItemPage(self.driver)

    def get_project_names_list(self):
        project_elements = self.driver.find_elements(By.CLASS_NAME, "jenkins-table__link")
        project_names = [element.text for element in project_elements]

        return project_names