

import pytest

import time

from selenium.webdriver import Keys


from selenium import webdriver
from selenium.webdriver.common.by import By




def test_login_page(browser):
    print(browser.current_url)
    assert browser.current_url == 'http://localhost:8080/login?from=%2F'

@pytest.mark.skip
def test_user_name_fild(browser):
    print(browser.current_url)
    user_name_fild = browser.find_element(By.XPATH,"//input[@id='j_username']")
    user_name_fild.clear()
    time.sleep(2)
    user_name_fild.send_keys('admin')
    time.sleep(1)
    assert user_name_fild.get_attribute('value') == 'admin'

def test_create_new_item_icon(browser):
    create_new_item = browser.find_element(By.XPATH,"//a[@it='hudson.model.Hudson@32e2f63a']")
    time.sleep(2)
    assert create_new_item.is_displayed()

def test_create_new_item(browser):
    create_new_item = browser.find_element(By.XPATH, "//a[@it='hudson.model.Hudson@32e2f63a']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH,"//input[@id='name']")
    item_name_fild.send_keys('London')
    assert item_name_fild.get_attribute('value') == 'London'
