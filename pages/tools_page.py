from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ToolsPage(BasePage):
    ADD_JDK = (By.XPATH, "//button[contains(., 'Add JDK')]")
    JDK_INSTALLATION = (By.XPATH, "//button[contains(., 'JDK installations')]")
    JDK_NAME = (By.XPATH,
                "//*[@id='main-panel']/form/div[1]/section[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/input")
    JDK_HOME = (By.XPATH,
                "//*[@id='main-panel']/form/div[1]/section[2]/div[3]/div/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/input")

    def get_section_titles(self):
        section_titles = self.wait10.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'jenkins-section__title')]")))

        return [title.text.strip().lower() for title in section_titles]

    def get_page_description(self):
        description_on_the_page = self.wait10.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'jenkins-page-description')]"
            ))
        )

        return description_on_the_page.text

    def click_apply(self):
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()
        self.wait10.until(EC.visibility_of_element_located((By.ID, "notification-bar")))
        return self

    def click_save(self):
        self.driver.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()
        self.wait10.until(EC.url_contains("/manage/"))
        from pages.manage_page import ManagePage
        return ManagePage(self.driver)

    def get_success_message(self):
        bar = self.wait10.until(EC.visibility_of_element_located((By.ID, "notification-bar")))
        return bar.text

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def open_jdk_block(self):
        buttons = self.driver.find_elements(*self.ADD_JDK)
        if len(buttons) > 0 and buttons[0].is_displayed():
            return self
        toggle_locator = (By.XPATH, "//button[contains(@class, 'advanced-button') and contains(., 'JDK')]")
        element = self.wait10.until(EC.presence_of_element_located(toggle_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait10.until(EC.visibility_of_element_located(self.ADD_JDK))

        return self

    def click_add_jdk(self):
        add_btn = self.wait10.until(EC.presence_of_element_located(self.ADD_JDK))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_btn)
        self.driver.execute_script("arguments[0].click();", add_btn)
        return self

    def fill_jdk(self, name, java_home):
        name_element = (self.wait10.until(EC.visibility_of_element_located(self.JDK_NAME)))
        name_element.clear()
        name_element.send_keys(name)
        home_element = self.wait10.until(EC.visibility_of_element_located(self.JDK_HOME))
        home_element.clear()
        home_element.send_keys(java_home)

        return self

    def get_jdk_name(self):
        self.open_jdk_block()
        element = self.wait10.until(EC.presence_of_element_located(self.JDK_NAME))
        return element.get_attribute("value")

    def click_add_git(self):
        self.driver.find_element(By.XPATH, "//*[@id='main-panel']/form/div[1]/section[3]/div[2]/span/button]").click()
        return self
