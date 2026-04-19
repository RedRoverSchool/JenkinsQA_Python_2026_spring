import pytest
from selenium.webdriver.common.by import By


def sign_in(browser):
    browser.get("http://localhost:8080/")
    browser.find_element(By.XPATH, "//*[@id='j_username']").send_keys("admin")
    browser.find_element(By.XPATH, "//*[@id='j_password']").send_keys("admin")
    browser.find_element(By.XPATH, "//*[@id='main-panel']/div/form/button").click()

@pytest.mark.skip()
def test_exercise(browser):
    sign_in(browser)

    excepted_name = browser.find_element(By.XPATH, "//*[@id='main-panel']/div[2]/div/h1").text
    assert excepted_name == "Welcome to Jenkins!"







