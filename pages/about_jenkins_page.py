from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AboutJenkinsPage(BasePage):

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def get_title_text(self):
        return self.driver.find_element(By.XPATH, "//h1[@class='app-about-heading']").text

    def get_version_text(self):
        return self.driver.find_element(By.XPATH, "//p[@class='app-about-version']").text

    def get_table_rows_count(self):
        return len(self.driver.find_elements(By.XPATH, "//table[@class='jenkins-table sortable']//tbody/tr"))

    def is_jenkins_core_present(self):
        try:
            return self.driver.find_element(By.XPATH, "//td[contains(text(), 'org.jenkins-ci.main:jenkins-core')]").is_displayed()
        except NoSuchElementException:
            return False
