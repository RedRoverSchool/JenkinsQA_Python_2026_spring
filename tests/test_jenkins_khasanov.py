

import pytest

import time

from selenium.webdriver import Keys


from selenium import webdriver
from selenium.webdriver.common.by import By




def test_login_page(browser):#Провекрка страницы аторизации
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

def test_create_new_item_icon(browser):#Проверка отоюражения кнопки New Item
    create_new_item = browser.find_element(By.XPATH,"//a[@it='hudson.model.Hudson@32e2f63a']")
    time.sleep(2)
    assert create_new_item.is_displayed()

def test_create_new_item(browser):#Проверка ввода имени в поле ввода New Item
    create_new_item = browser.find_element(By.XPATH, "//a[@it='hudson.model.Hudson@32e2f63a']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH,"//input[@id='name']")
    item_name_fild.send_keys('London')
    assert item_name_fild.get_attribute('value') == 'London'


def test_select_type_item(browser):#Проверка что выбранный тип активировался после нажатия на него
    create_new_item = browser.find_element(By.XPATH, "//a[@it='hudson.model.Hudson@32e2f63a']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH, "//input[@id='name']")
    item_name_fild.send_keys('London')

    folder_type = browser.find_element(By.XPATH,"//span[text()='Folder']")
    folder_type.click()
    time.sleep(2)
    activ_type = browser.find_element(By.XPATH,"//li[@class='com_cloudbees_hudson_plugins_folder_Folder active']")
    assert activ_type.get_attribute('class') == 'com_cloudbees_hudson_plugins_folder_Folder active'

