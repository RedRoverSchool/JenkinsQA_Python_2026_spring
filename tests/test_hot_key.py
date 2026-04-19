import pytest
from selenium.webdriver import Keys

from tests.test_automationexercise import sign_in
from selenium.webdriver.common.by import By


@pytest.mark.skip()
def test_hot_key(browser):
    sign_in(browser)
    browser.find_element(By.XPATH, "//*[@id='jenkins']").send_keys(Keys.LEFT_CONTROL + "k")
    exected_element = browser.find_element(By.XPATH, "//*[@id='command-bar']").is_displayed()
    assert exected_element == True


