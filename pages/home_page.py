from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.folder_page import FolderPage
from pages.freestyle_config_page import FreestyleConfigPage
from pages.manage_page import ManagePage
from pages.multibranch_pipeline_page import MultiBranchPipelinePage
from pages.multiconfiguration_project_page import MulticonfigurationProjectPage
from pages.new_item_page import NewItemPage
from pages.rename_project_page import RenameProjectPage
from pages.pipeline_project_page import PipelineProjectPage
from pages.base_project_page import BaseProjectPage
from pages.new_view_page import NewViewPage


class HomePage(BasePage):
    def click_new_item(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))
        ).click()

        return NewItemPage(self.driver)

    def click_manage_gear(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@href = '/manage']"))
        ).click()

        return ManagePage(self.driver)

    def get_project_names_list(self):
        project_elements = self.driver.find_elements(By.CLASS_NAME, "jenkins-table__link")
        project_names = [element.text for element in project_elements]

        return project_names

    def click_schedule_build(self, job_name: str):
        self.driver.find_element(By.XPATH, f"//tr/td[7]//a[@tooltip='Schedule a Build for {job_name}']").click()

        return self

    def get_names_jobs_list_build_queue(self) -> list:
        list_elements = self.driver.find_elements(By.XPATH,
                                                  f" //div[@class='pane-content']//tr/td/a[@class='model-link inside tl-tr']")
        return [name_job.text for name_job in list_elements]

    def show_dropdown_menu_from_profile_icon(self):
        user_icon = self.wait10.until(EC.visibility_of_element_located((By.ID, "root-action-UserAction")))
        ActionChains(self.driver).move_to_element(user_icon).perform()

        return self

    def click_dropdown_menu_sign_out(self):
        xpath_logout = "//a[contains(@href, '/logout')]"
        sign_out_button = self.wait10.until(EC.element_to_be_clickable((By.XPATH, xpath_logout)))

        try:
            sign_out_button.click()
        except StaleElementReferenceException:
            self.wait10.until(EC.element_to_be_clickable((By.XPATH, xpath_logout))).click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)

    def sign_out(self):
        return self.show_dropdown_menu_from_profile_icon().dropdown_menu_sign_out_click()

    def is_jenkins_icon_visible(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#jenkins-head-icon"))
        ).is_displayed()

    def click_pipeline_job(self, job_name: str):
        self.wait5.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@href='job/{job_name}/'])[1]"))).click()

        return PipelineProjectPage(self.driver)

    def click_multibranch_pipeline_job(self, job_name: str):
        self.wait5.until(EC.element_to_be_clickable((By.XPATH, f"(//a[@href='job/{job_name}/'])[1]"))).click()

        return MultiBranchPipelinePage(self.driver)

    def click_project_name(self, job_name: str, job_type="project"):
        self.driver.find_element(By.XPATH, f"//*[@id='job_{job_name}']/td[3]/a").click()
        if job_type == "project":
            return BaseProjectPage(self.driver)
        elif job_type == "folder":
            return FolderPage(self.driver)
        return None

    def get_project_name(self):

        return self.wait5.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".jenkins-table__link >span:first-child"))
        ).text

    def open_project_dropdown(self, job_name):
        self.wait10.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="job/{job_name}/"] .jenkins-menu-dropdown-chevron'))
        ).click()

        return self

    def click_project_rename(self, job_name):
        self.wait10.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Rename'))).click()

        return RenameProjectPage(self.driver)

    def click_configure_link(self):
        self.wait10.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Configure'))).click()

        return FreestyleConfigPage(self.driver)

    def new_job_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='newJob']"))
        ).click()

        return NewItemPage(self.driver)

    def click_new_view_link(self):
        self.wait10.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[href = '/newView']"))).click()

        return NewViewPage(self.driver)

    def get_view_names_list(self):
        tabs = self.driver.find_elements(By.XPATH, "//div[@class='tab']/a[not(@tooltip='New View')] ")
        tab_names = [element.text for element in tabs]

        return tab_names

    def click_search_icon(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.ID, "root-action-SearchAction"))).click()

        return self

    def set_created_project_name(self, name):
        self.wait10.until(EC.visibility_of_element_located((By.ID, "command-bar"))).send_keys(name)

        return self

    def click_searched_project_name(self, name):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/job/{name}/')]"))).click()

        return MulticonfigurationProjectPage(self.driver)

    def open_project_dropdown(self, job_name):
        self.wait10.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="job/{job_name}/"] .jenkins-menu-dropdown-chevron'))
        ).click()
        return self

    def click_add_new_view_tab(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/newView']"))
        ).click()
        from pages.new_view_page import NewViewPage
        return NewViewPage(self.driver)

    def get_view_tab_names(self):
        self.wait10.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tabBar")))
        tabs = self.driver.find_elements(By.CSS_SELECTOR, ".tabBar .tab a")
        return [tab.text for tab in tabs if tab.text not in ["+", "All", ""]]

    def is_project_exist(self, project_name):
        try:
            WebDriverWait(self.driver,5).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[span[text()='{project_name}']]")))
            return True
        except TimeoutException:
            return False

    def click_item_in_profile_icon_dropdown_menu(self, name):
        item_locator = (By.XPATH, f'//a[contains(@href, "{name}")]')

        self.show_dropdown_menu_from_profile_icon()
        self.wait10.until(EC.element_to_be_clickable(item_locator)).click()

        return pages.profile_page.ProfilePage(self.driver)
