from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.view_page import ViewPage

class NewViewPage(BasePage):
    def set_new_view_name(self,new_view_name):
        self.wait10.until(EC.visibility_of_element_located((By.ID,'name'))).send_keys(new_view_name)

        return self

    def check_my_view_radio_btn(self):
        self.wait10.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='hudson.model.MyView']" ))).click()

        return self

    def click_create_btn(self):
        self.wait10.until(EC.visibility_of_element_located((By.ID,'ok'))).click()

        return ViewPage(self.driver)
