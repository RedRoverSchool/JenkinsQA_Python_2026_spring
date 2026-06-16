import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage

@pytest.mark.parametrize("display_name, description", [
    ("JenkinsQA_Python_2026", "Very good Python automation course"),
    ("JenkinsQA_Java_2026", "Very good Java automation course"),
    ("JenkinsQA_JavaScript_2026", "Very good Javascript automation course")
])

@pytest.mark.dependency()
def test_create_org_folder(browser, display_name, description):
    project_page = (
        HomePage(browser)
        .click_new_item()
        .set_org_folder_and_ok_click("Red Rover")
        .set_display_name(display_name)
        .set_description_name(description)
        .click_save()
    )

    assert project_page.get_display_name() == display_name
    assert project_page.get_description() == description


@pytest.mark.dependency(depends=["test_create_org_folder"])
def test_open_configuration_1(browser):

    browser.find_element(By.CLASS_NAME, "jenkins-mobile-hide").click()
    browser.find_element(By.CLASS_NAME, "jenkins-menu-dropdown-chevron").click()
    configure = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='jenkins-dropdown__item '][1]")))
    configure.click()
    conf_page_title = browser.find_element(By.ID, "general").text

    assert conf_page_title == "General"
