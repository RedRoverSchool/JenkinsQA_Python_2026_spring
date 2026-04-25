from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pytest

from common.jenkins_utils import login


@pytest.fixture()
def disable_theme_manager(browser):

    browser.find_element(By.ID, 'root-action-ManageJenkinsAction').click()

    browser.find_element(By.CSS_SELECTOR, 'a[href="pluginManager"]').click()

    browser.find_element(By.XPATH, '//a[contains(. , "Installed plugins")]').click()

    theme_manager_plugin = browser.find_element(By.CSS_SELECTOR, 'tr[data-plugin-name="Theme Manager"] input')
    if theme_manager_plugin.get_attribute('checked'):
        browser.find_element(By.CSS_SELECTOR, 'tr[data-plugin-name="Theme Manager"] span.jenkins-toggle-switch').click()
        browser.find_element(By.NAME, 'Submit').click()
        WebDriverWait(browser, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text() = 'Sign in to Jenkins']"))
        )    # ждем долгую перезагрузку дженкинса, неявных 5 секунд ожидания мало.
        login(browser)
    else:
        browser.find_element(By.CLASS_NAME, 'app-jenkins-logo').click()



def test_quick_change_theme_not_able(browser, disable_theme_manager):

    ActionChains(browser).move_to_element(browser.find_element(By.XPATH, '//a[@href="/user/admin"]')).perform()

    assert not browser.find_elements(By.ID, 'account-theme-picker'), "Error: quick change theme field is showed"
