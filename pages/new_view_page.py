from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NewViewPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    LIST_VIEW_RADIO = (By.XPATH, "//label[contains(text(), 'List View')]")
    MY_VIEW_RADIO = (By.XPATH, "//label[contains(text(), 'My View')]")  # Додано
    CREATE_BUTTON = (By.ID, "ok")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Save')]")

    def set_new_view_name(self, name: str):
        self.wait10.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        return self

    def select_list_view(self):
        self.wait10.until(EC.element_to_be_clickable(self.LIST_VIEW_RADIO)).click()
        return self

    def is_list_view_displayed(self):
        return self.wait10.until(EC.visibility_of_element_located(self.LIST_VIEW_RADIO)).is_displayed()

    def is_my_view_displayed(self):
        return self.wait10.until(EC.visibility_of_element_located(self.MY_VIEW_RADIO)).is_displayed()
    
    def check_my_view_radio_btn(self):
        self.wait10.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='hudson.model.MyView']" ))).click()

    def is_create_button_disabled(self):
        button = self.driver.find_element(*self.CREATE_BUTTON)
        return not button.is_enabled() or button.get_attribute("disabled") is not None

    def click_create_btn(self):
        self.wait10.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()
        self.wait10.until(EC.url_contains("configure"))
        return self

    def click_save(self):
        self.wait10.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        return self
