from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.project_page import ProjectPage


class FolderPage(ProjectPage):

    def get_config_description(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "view-message"))).text

    def new_item_click(self):
        from pages.new_item_page import NewItemPage

        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/newJob')]"))
        ).click()

        return NewItemPage(self.driver)

    def get_full_folder_name(self):
        self.wait10.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".job-index-headline.page-headline")))
        return [line for line in self.driver.find_element(By.ID, "main-panel").text.split('\n') if
                line.startswith("Full folder name: ")][0]

    def get_new_item_name(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='job-index-headline page-headline']"))).text
