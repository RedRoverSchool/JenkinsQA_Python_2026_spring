import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.dependency()
def test_create_org_folder(browser):
    browser.find_element(By.XPATH, "//*[contains(concat(' ', @href, ' '), ' newJob ')]" ).click()
    browser.find_element(By.ID, "name").send_keys("Red Rover")
    browser.find_element(By.XPATH, "//*[@class='label'][.='Organization Folder']").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.NAME, "_.displayNameOrNull").send_keys("JenkinsQA_Python_2026")
    browser.find_element(By.NAME, "_.description").send_keys("Very good Python automation course")
    browser.find_element(By.NAME, "Submit").click()

    display_name = browser.find_element(By.CSS_SELECTOR, "h1.job-index-headline").text.strip()
    description = browser.find_element(By.ID, "view-message").text.strip()

    assert display_name == "JenkinsQA_Python_2026"
    assert description == "Very good Python automation course"


@pytest.mark.dependency(depends=["test_create_org_folder"])
def test_open_configuration_1(browser):

    browser.find_element(By.CLASS_NAME, "jenkins-mobile-hide").click()
    browser.find_element(By.CLASS_NAME, "jenkins-menu-dropdown-chevron").click()
    configure = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='jenkins-dropdown__item '][1]")))
    configure.click()
    conf_page_title = browser.find_element(By.ID, "general").text

    assert conf_page_title == "General"
