from pages.base_page import BasePage


class ProfilePage(BasePage):
    def get_current_url(self):
        return self.driver.current_url
