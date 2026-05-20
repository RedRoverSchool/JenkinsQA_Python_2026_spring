import pytest
from selenium.webdriver.common.by import By

from pages.home_page import HomePage


@pytest.mark.parametrize("themes", ["none", "dark", "dark-system"])
def test_appearance_theme(browser, themes):

    theme = (
        HomePage(browser)
             .click_manage_gear()
             .click_appearance()
             .set_theme(themes)
             .click_apply_button()
             .get_theme()
    )

    assert themes == theme


@pytest.mark.skip()
def test_appearance_show_pipeline_stages(browser):
    browser.find_element(By.XPATH, "//a[@id='root-action-ManageJenkinsAction']").click()
    browser.find_element(By.XPATH, "//a[@href='appearance']").click()

    checkbox_stages_1 = (browser.find_element
                  (By.XPATH, '//input[@name="_.showGraphOnJobPage"]/parent::span'))
    browser.execute_script("arguments[0].scrollIntoView(true);", checkbox_stages_1)
    checkbox_stages_1.click()

    browser.get("http://localhost:8080/")
    job_link = browser.find_element(By.XPATH, '//a[@href="job/test/"]')
    browser.execute_script("arguments[0].click();", job_link)
    stages_loc = browser.find_element(By.XPATH, "//a[@href='multi-pipeline-graph']")
    assert stages_loc.is_displayed()
