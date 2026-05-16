from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ToolsPage(BasePage):
    def get_section_titles(self):
        section_titles = self.wait10.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'jenkins-section__title')]")))

        return [title.text.strip().lower() for title in section_titles]

    def get_page_description(self):
        description_on_the_page = self.wait10.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'jenkins-page-description')]"
            ))
        )

        return description_on_the_page.text

