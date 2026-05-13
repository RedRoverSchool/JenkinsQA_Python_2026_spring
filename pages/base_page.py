from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)
        self.wait5 = WebDriverWait(driver, 5)

    def go_home_page(self):
        from pages.home_page import HomePage

        self.wait10.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "jenkins-mobile-hide"))
        ).click()

        return HomePage(self.driver)
