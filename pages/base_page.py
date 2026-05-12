from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)

    def go_home_page(self):
        from pages.home_page import HomePage

        self.driver.execute_script("""
            var logo = document.querySelector('.jenkins-mobile-hide');
            if (logo) logo.click();
        """)

        return HomePage(self.driver)