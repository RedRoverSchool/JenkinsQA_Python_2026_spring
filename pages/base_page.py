from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pages

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)
        self.wait5 = WebDriverWait(driver, 5)

    def go_home_page(self):
        self.driver.execute_script("""
            var logo = document.querySelector('.jenkins-mobile-hide');
            if (logo) logo.click();
        """)

        return pages.home_page.HomePage(self.driver)

    def get_breadcrumb_texts_list(self):
        try:
            breadcrumb_elements = self.wait10.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".jenkins-breadcrumbs__list-item"))
            )
            return [crumb.text for crumb in breadcrumb_elements if crumb.text.strip()]
        except:
            return []
