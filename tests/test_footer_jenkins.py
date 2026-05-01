import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_footer_jenkins_version(browser):

    version_button = browser.find_element(By.XPATH, "//button[contains(@class, 'jenkins_ver')]")

    assert version_button.is_displayed()
    assert version_button.text == "Jenkins 2.541.3"


def test_about_jenkins(browser):

    wait = WebDriverWait(browser, 5)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jenkins_ver')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='About Jenkins']"))).click()

    title = browser.find_element(By.XPATH, "//h1[@class='app-about-heading']").text
    version = browser.find_element(By.XPATH, "//p[@class='app-about-version']").text

    assert "About Jenkins - Manage Jenkins - Jenkins" in browser.title
    assert "/manage/about/" in browser.current_url
    assert title == "Jenkins"
    assert version == "Version 2.541.3"
