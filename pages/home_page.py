from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import BasePage
from pages.manage_page import ManagePage
from pages.multibranch_pipeline_page import MultiBranchPipelinePage
from pages.new_item_page import NewItemPage

from pages.pipeline_project_page import PipelineProjectPage
from pages.project_page import ProjectPage



class HomePage(BasePage):
    def new_item_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))
        ).click()

        return NewItemPage(self.driver)

    def manage_gear_click(self):
        self.wait10.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@href = '/manage']"))
        ).click()

        return ManagePage(self.driver)

    def get_project_names_list(self):
        project_elements = self.driver.find_elements(By.CLASS_NAME, "jenkins-table__link")
        project_names = [element.text for element in project_elements]

        return project_names

    def schedule_build_click(self, job_name: str):
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

    def dropdown_menu_sign_out_click(self):
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

    def project_name_click(self, job_name: str):
        self.driver.find_element(By.XPATH, f"//*[@id='job_{job_name}']/td[3]/a").click()

        return ProjectPage(self.driver)
