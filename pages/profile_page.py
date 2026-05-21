from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProfilePage(BasePage):
    def is_profile_page_opened(self):
        self.wait10.until(EC.url_contains("/user/"))

        return "/user/" in self.driver.current_url

    def is_profile_header_visible(self):
        profile_header_locator = (By.TAG_NAME, "h1")
        return self.wait10.until(
            EC.visibility_of_element_located(profile_header_locator)
        ).is_displayed()
