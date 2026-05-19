from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pages
from pages.base_page import BasePage
from pages.rename_project_page import RenameProjectPage


class BaseProjectPage(BasePage):
    def get_description(self):
        return self.wait10.until(EC.visibility_of_element_located((By.ID, "description-content"))).text

    def get_project_name(self):
        return self.wait10.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".job-index-headline.page-headline"))
        ).text

    def click_project_configure(self, job_type="project"):
        self.driver.find_element(By.XPATH, "//a[contains(., 'Configure')]").click()
        if job_type == "project":
            return pages.base_config_page.BaseConfigPage(self.driver)
        elif job_type == "folder":
            return pages.folder_config_page.FolderConfigPage(self.driver)
        elif job_type == "freestyle_project":
            return pages.freestyle_config_page.FreestyleConfigPage(self.driver)
        elif job_type == "multibranch_pipeline":
            return pages.multibranch_pipeline_config_page.MultiBranchPipelineConfigPage(self.driver)
        elif job_type == "multiconfiguration_project":
            return pages.multiconfiguration_project_config_page.MulticonfigurationProjectConfigPage(self.driver)
        elif job_type == "pipeline":
            return pages.pipeline_config_page.PipelineConfigPage(self.driver)
        return None

    def click_rename_project(self):
        self.wait10.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Rename'))).click()

        return RenameProjectPage(self.driver)

    def click_add_description_link(self):
        self.wait10.until(EC.visibility_of_element_located((By.ID, "description-link"))).click()

        return self

    def add_description(self, new_description):
        self.wait10.until(EC.visibility_of_element_located((By.NAME, "description"))).send_keys(new_description)
        self.wait10.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

        return self

    def click_delete(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-title, 'Delete')]"))).click()

        return self

    def click_cancel_delete_button(self):
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='cancel']"))).click()

        return self

    def click_confirm_delete_button(self):
        from pages.home_page import HomePage
        self.wait10.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='ok']"))).click()

        return HomePage(self.driver)
