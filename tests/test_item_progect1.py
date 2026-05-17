import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.dependency()
def test_open_url(browser):
    assert  browser.current_url == 'http://localhost:8080/login?from=%2F'

@pytest.mark.dependency(depends=["test_open_url"])
def test_create_new_item_icon(browser):#Проверка отоюражения кнопки New Item
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH,"//a[@href='/view/all/newJob']")
    time.sleep(2)
    assert create_new_item.is_displayed()

@pytest.mark.dependency()
def test_create_new_item(browser):#Проверка ввода имени в поле ввода New Item
    time.sleep(2)
    create_new_item = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']")
    create_new_item.click()
    time.sleep(2)
    item_name_fild = browser.find_element(By.XPATH,"//input[@id='name']")
    item_name_fild.send_keys('London')
    time.sleep(2)
    folder_type = browser.find_element(By.XPATH,"//span[text()='Folder']")
    folder_type.click()
    time.sleep(2)
    assert item_name_fild.get_attribute('value') == 'London'
    button_OK = browser.find_element(By.XPATH,"//button[@id='ok-button']")
    button_OK.click()

@pytest.mark.dependency(depends=["test_create_new_item"])
def test_open_configuration(browser):
    n = browser.find_element(By.XPATH,"//li[@data-type='breadcrumb-item'][1]").get_attribute('value')
    assert browser.current_url == f'http://localhost:8080/job/{n}/configure'