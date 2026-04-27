import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation_to_tools(browser):
    open_manage_jenkins(browser)
    open_tools(browser)

    text = "Configure tools, their locations and automatic installers."

    text_on_tools_page = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'jenkins-page-description')]"
        ))
    )

    assert text in text_on_tools_page.text
    assert f"/manage/configureTools/" in browser.current_url


@pytest.mark.skip(reason="Flaky test in CI - stale element")
def test_configuration_sections(browser):
    open_manage_jenkins(browser)
    open_tools(browser)

    section_titles = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'jenkins-section__title')]")))

    expected_section_titles = ['maven configuration', 'jdk installations', 'git installations', 'gradle installations', 'ant installations', 'maven installations']
    actual_section_titles = [title.text.strip().lower() for title in section_titles]
    assert actual_section_titles == expected_section_titles



def open_tools(browser):
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//*[@href='configureTools']"
        ))
    ).click()


def open_manage_jenkins(browser):
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//*[@id='root-action-ManageJenkinsAction']"
        ))
    ).click()