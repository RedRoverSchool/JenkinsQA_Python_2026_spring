from selenium.webdriver.common.by import By


def _get_rest_api_link(driver):
    locator = (By.XPATH, '//footer//a[text()="REST API"]')
    return driver.find_element(*locator)


def _get_manage_jenkins_button(driver):
    manage_jenkins_button = (By.ID, 'root-action-ManageJenkinsAction')
    return driver.find_element(*manage_jenkins_button)


def test_checking_the_button_on_dashboard(browser):
    rest_api_link = _get_rest_api_link(browser)

    assert rest_api_link.is_displayed()


def test_checking_the_button_on_nodes(browser):
    _get_manage_jenkins_button(browser).click()
    browser.find_element(By.CSS_SELECTOR, 'a[href="computer"]').click()

    rest_api_link = _get_rest_api_link(browser)

    assert rest_api_link.is_displayed()


def test_checking_the_button_on_credentials(browser):
    _get_manage_jenkins_button(browser).click()
    browser.find_element(By.CSS_SELECTOR, 'a[href="credentials"]').click()

    rest_api_link = _get_rest_api_link(browser)

    assert rest_api_link.is_displayed()