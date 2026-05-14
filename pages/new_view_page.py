from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NewViewPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    LIST_VIEW_RADIO = (By.XPATH, "//label[contains(text(), 'List View')]")
    CREATE_BUTTON = (By.ID, "ok")

    def enter_name(self, name: str):
        self.wait10.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        return self

    def select_list_view(self):
        self.wait10.until(EC.element_to_be_clickable(self.LIST_VIEW_RADIO)).click()
        return self

    def is_create_button_enabled(self):
        return self.driver.find_element(*self.CREATE_BUTTON).is_enabled()

    def click_create(self):
        create_btn = self.wait10.until(EC.element_to_be_clickable(self.CREATE_BUTTON))
        create_btn.click()
        self.wait10.until(EC.url_contains("configure"))
        return self