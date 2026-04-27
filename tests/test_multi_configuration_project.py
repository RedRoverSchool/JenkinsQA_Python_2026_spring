import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

multiconfiguration_project_name = "MultiConfigName"

def test_verify_status_switching_enable_button(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(multiconfiguration_project_name)
    browser.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.NAME, "Submit").click()

    browser.find_element(By.XPATH, "//a[@href='/job/" + multiconfiguration_project_name + "/configure']").click()
    browser.find_element(By.CSS_SELECTOR, "#toggle-switch-enable-disable-project > label").click()
    browser.find_element(By.NAME, "Submit").click()

    actual_disable_text = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "enable-project"))).text

    assert "This project is currently disabled" in actual_disable_text


def test_verify_enable_toogle_has_tooltip(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(multiconfiguration_project_name)
    browser.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()
    browser.find_element(By.ID, "ok-button").click()

    enabled_toogle = browser.find_element(By.ID, "toggle-switch-enable-disable-project")

    actions = ActionChains(browser)
    actions.move_to_element(enabled_toogle).perform()

    toggle_tooltip = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "tippy-content"))).text

    assert toggle_tooltip == "Enable or disable the current project"

@pytest.mark.parametrize("special_characters ",[
    "!", "%", "&", "#", "@", "*", "?", "^", "|", "/", "]", "["
])
def test_create_item_with_special_characters(browser, special_characters):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(f"{multiconfiguration_project_name}{special_characters}")
    browser.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "itemname-invalid"))).text

    expected_error_message = f"‘{special_characters}’ is an unsafe character"
    assert error_message == "» " + f"‘{special_characters}’ is an unsafe character"

    browser.find_element(By.ID, "ok-button").click()
    assert browser.find_element(By.TAG_NAME, "p").text == expected_error_message
