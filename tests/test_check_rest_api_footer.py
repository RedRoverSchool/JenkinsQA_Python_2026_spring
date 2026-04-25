import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Локаторы
REST_API_LINK = (By.XPATH, '//footer//a[text()="REST API"]')
MANAGE_JENKINS_BUTTON = (By.ID, 'root-action-ManageJenkinsAction')
NODES_LINK = (By.CSS_SELECTOR, 'a[href="computer"]')
CREDENTIALS_LINK = (By.CSS_SELECTOR, 'a[href*="credentials"]')


def check_rest_api_visible(driver):
    """Проверка наличия ссылки 'REST API' в футере страницы"""
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(REST_API_LINK)
    )

    assert element.is_displayed()
    assert element.text == "REST API"

@pytest.mark.smoke
def test_rest_api_on_dashboard(browser):
    """Проверка наличия отображения 'REST API' на главной странице"""
    check_rest_api_visible(browser)


@pytest.mark.smoke
def test_rest_api_on_nodes(browser):
    """Проверка наличия отображения 'REST API' на странице 'Nodes'"""
    browser.find_element(*MANAGE_JENKINS_BUTTON).click()
    browser.find_element(*NODES_LINK).click()

    check_rest_api_visible(browser)


@pytest.mark.smoke
def test_rest_api_on_credentials(browser):
    """Проверка наличия отображения 'REST API' на странице 'Credentials'"""
    browser.find_element(*MANAGE_JENKINS_BUTTON).click()
    browser.find_element(*CREDENTIALS_LINK).click()

    check_rest_api_visible(browser)