import pytest
from selenium.webdriver.common.by import By

def test_appearance_to_dark(browser):
    themes={'none': 'dark', 'dark': 'dark-system', 'dark-system': 'none'}
    browser.find_element(By.XPATH, "//a[@id='root-action-ManageJenkinsAction']").click()
    browser.find_element(By.XPATH, "//a[@href='appearance']").click()

    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    browser.find_element(By.XPATH, f'//div[@data-theme="{themes[theme]}"]/parent::label').click()

    theme_new = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme != theme_new


def test_appearance_to_dark_system(browser):
    themes = {'none': 'dark', 'dark': 'dark-system', 'dark-system': 'none'}
    browser.find_element(By.XPATH, "//a[@id='root-action-ManageJenkinsAction']").click()
    browser.find_element(By.XPATH, "//a[@href='appearance']").click()

    browser.find_element(By.XPATH, '//div[@data-theme="dark"]/parent::label').click()
    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    browser.find_element(By.XPATH, f'//div[@data-theme="{themes[theme]}"]/parent::label').click()

    theme_new = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme != theme_new


def test_appearance_to_light(browser):
    themes = {'none': 'dark', 'dark': 'dark-system', 'dark-system': 'none'}
    browser.find_element(By.XPATH, "//a[@id='root-action-ManageJenkinsAction']").click()
    browser.find_element(By.XPATH, "//a[@href='appearance']").click()

    browser.find_element(By.XPATH, '//div[@data-theme="dark-system"]/parent::label').click()
    theme = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    browser.find_element(By.XPATH, f'//div[@data-theme="{themes[theme]}"]/parent::label').click()

    theme_new = browser.find_element(By.TAG_NAME, "html").get_attribute("data-theme")

    assert theme != theme_new


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



