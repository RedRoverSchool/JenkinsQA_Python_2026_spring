import pytest
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.dependency()
def test_checking_dropdown_partial_match(browser):
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'root-action-ManageJenkinsAction'))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'settings-search-bar'))
    ).send_keys('t')
    items = browser.find_elements(
        By.XPATH,
        '//*[contains(@class, "jenkins-search__results-container--visible")]//a[contains(translate(., "T", "t"), "t")]'
    )

    assert len(items) > 1


@pytest.mark.dependency(depends=["test_checking_dropdown_partial_match"])
def test_checking_dropdown_full_match(browser):
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'root-action-ManageJenkinsAction'))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'settings-search-bar'))
    ).send_keys('Security')
    item = browser.find_element(
        By.XPATH,
        '//*[contains(@class,"jenkins-search__results-container--visible")]//a[normalize-space()="Security"]'
    )

    assert item.get_attribute('textContent').strip() == 'Security'


@pytest.mark.skip(reason="ER_10.002.03")
def test_clear_search_field_and_verify_empty(browser):
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'root-action-ManageJenkinsAction'))
    ).click()

    field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'settings-search-bar'))
    )
    field.send_keys(Keys.CONTROL + 'a')
    field.send_keys(Keys.BACK_SPACE)

    field.send_keys('Manage Jenkins')
    field.clear()

    assert field.get_attribute('value') == ''
    assert 'No results' in browser.find_element(By.CSS_SELECTOR, '.jenkins-search__results-container').text