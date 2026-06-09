from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pages
import time

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait10 = WebDriverWait(driver, timeout)
        self.wait5 = WebDriverWait(driver, 5)

    def go_home_page(self):
        time.sleep(0.5)
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

    def refresh_page(self):
        self.driver.refresh()

        return self

    def click_main_panel(self):
        self.driver.find_element(By.ID, 'main-panel').click()

        return self

    def get_theme(self) -> str:
        """`none` значит что установлена тема Light"""

        return self.driver.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    def get_jenkins_version(self):
        return self.driver.find_element(By.XPATH, "//button[contains(@class, 'jenkins_ver')]").text

    def click_jenkins_version_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jenkins_ver')]"))).click()
        return self

    def click_about_jenkins(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='About Jenkins']"))).click()
        return self

    def get_cursor_type(self):
        return self.driver.find_element(By.ID, "root-action-ManageJenkinsAction").value_of_css_property("cursor")