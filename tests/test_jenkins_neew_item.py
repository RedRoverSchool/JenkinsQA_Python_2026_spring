

import pytest

import time

from selenium.webdriver import Keys


from selenium import webdriver
from selenium.webdriver.common.by import By




def test_login_page(browser):#Провекрка страницы аторизации
    print(browser.current_url)
    assert browser.current_url == 'http://localhost:8080/login?from=%2F'

@pytest.mark.skip
def test_user_name_fild(browser):#Проверка поля ввода логина
    print(browser.current_url)
    user_name_fild = browser.find_element(By.XPATH,"//input[@id='j_username']")
    user_name_fild.clear()
    time.sleep(2)
    user_name_fild.send_keys('admin')
    time.sleep(1)
    assert user_name_fild.get_attribute('value') == 'admin'

def test_create_new_item_icon(browser):#Проверка отоюражения кнопки New Item
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH,"//a[@href='/view/all/newJob']")
    time.sleep(2)
    assert create_new_item.is_displayed()

def test_create_new_item(browser):#Проверка ввода имени в поле ввода New Item
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH,"//input[@id='name']")
    item_name_fild.send_keys('London')
    assert item_name_fild.get_attribute('value') == 'London'


def test_select_type_item(browser):#Проверка что выбранный тип активировался после нажатия на него
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH, "//input[@id='name']")
    item_name_fild.send_keys('London')

    folder_type = browser.find_element(By.XPATH,"//span[text()='Folder']")
    folder_type.click()
    time.sleep(2)
    activ_type = browser.find_element(By.XPATH,"//li[@class='com_cloudbees_hudson_plugins_folder_Folder active']")
    assert activ_type.get_attribute('class') == 'com_cloudbees_hudson_plugins_folder_Folder active'


def test_open_configuration_page(browser):
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH, "//input[@id='name']")
    item_name_fild.send_keys('London')
    n = item_name_fild.get_attribute('value')
    folder_type = browser.find_element(By.XPATH, "//span[text()='Folder']")
    folder_type.click()
    time.sleep(2)
    button_OK = browser.find_element(By.XPATH,"//button[@id='ok-button']")
    button_OK.click()
    assert browser.current_url == f'http://localhost:8080/job/{n}/configure'

def test_input_configuration_page(browser):
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH, "//input[@id='name']")
    item_name_fild.send_keys('London')
    n = item_name_fild.get_attribute('value')
    folder_type = browser.find_element(By.XPATH, "//span[text()='Folder']")
    folder_type.click()
    time.sleep(2)
    button_OK = browser.find_element(By.XPATH, "//button[@id='ok-button']")
    button_OK.click()
    inp_disp_name = browser.find_element(By.XPATH,"//input[@type='text']")
    inp_disp_name.send_keys('Display name')
    assert inp_disp_name.get_attribute('value') == 'Display name'
    descrip_text = browser.find_element(By.XPATH,"//textarea[@name='_.description']")
    descrip_text.send_keys('Description huyuuv bvtvvryvyrv yvyt7vvh')
    assert descrip_text.get_attribute('value') == 'Description huyuuv bvtvvryvyrv yvyt7vvh'
    btn_save = browser.find_element(By.XPATH,"//button[@name='Submit']")
    btn_save.click()
    time.sleep(4)
    assert browser.current_url == f'http://localhost:8080/job/{n}/'


