from selenium.webdriver.common.by import By
import pytest


@pytest.mark.skip()
def test_apply_button_folder_config(browser):
    new_item_button = browser.find_element(By.XPATH, "//a[contains(., 'New Item')]")
    new_item_button.click()
    assert "/view/all/newJob" in browser.current_url
    name_input = browser.find_element(By.XPATH, "//input[@id='name']")
    name_input.send_keys("TestName")
    assert  name_input.get_attribute("value") ==  "TestName"
    folder = browser.find_element(By.XPATH, "//li[contains(@class,'folder_Folder')]")
    folder.click()
    ok_button = browser.find_element(By.XPATH, "//button[contains(.,'OK')]")
    ok_button.click()
    assert "/job/TestName/configure" in browser.current_url
    new_name_input = browser.find_element(By.NAME, "_.displayNameOrNull")
    new_name_input.send_keys("TestName1")
    assert new_name_input.get_attribute("value") == "TestName1"
    apply_button = browser.find_element(By.NAME, "Apply")
    apply_button.click()
    assert "/job/TestName/configure" in browser.current_url
    assert "TestName1" in browser.page_source

