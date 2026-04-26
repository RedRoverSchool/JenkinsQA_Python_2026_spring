import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_footer_jenkins_version(browser):
    """Проверка отображения версии Jenkins в футере"""
    version_button = browser.find_element(By.XPATH, "//button[contains(@class, 'jenkins_ver')]")

    assert version_button.is_displayed()
    assert version_button.text == "Jenkins 2.541.3"


def test_footer_jenkins_version_dropdown(browser):
    """Проверка наличия About Jenkins, Get involved, Website в dropdown при клике на Jenkins версию в футере"""
    version_button = browser.find_element(By.XPATH, "//button[contains(@class, 'jenkins_ver')]")
    version_button.click()

    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "jenkins-dropdown"),
            "About Jenkins"
        )
    )

    dropdown_items = browser.find_elements(By.CLASS_NAME, "jenkins-dropdown__item")
    dropdown_items_list = [item.text.strip() for item in dropdown_items]

    assert "About Jenkins" in dropdown_items_list
    assert "Get involved" in dropdown_items_list
    assert "Website" in dropdown_items_list


@pytest.mark.parametrize("link_text, expected_url_part, expected_title", [
    ("About Jenkins", "/manage/about/", "About Jenkins - Manage Jenkins - Jenkins"),
    ("Get involved", "jenkins.io/participate", "Participate and Contribute"),
    ("Website", "jenkins.io", "Jenkins"),
])
def test_jenkins_version_dropdown_links(browser, link_text, expected_url_part, expected_title):
    """Проверка переходов по ссылкам About Jenkins, Get involved, Website из dropdown в футере"""
    wait = WebDriverWait(browser, 5)

    version_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jenkins_ver')]"))
    )
    version_button.click()

    link = wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='{link_text}']"))
    )
    link.click()

    wait.until(lambda d: expected_url_part in d.current_url)

    assert expected_url_part in browser.current_url
    assert expected_title in browser.title
