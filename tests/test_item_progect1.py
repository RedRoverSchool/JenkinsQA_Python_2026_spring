import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.dependency()
def test_open_url(browser):
    print(browser.current_url)
    assert  browser.current_url == 'http://localhost:8080/login?from=%2F'

@pytest.mark.dependency(depends=["test_open_url"])
def test_create_new_item_icon(browser):#Проверка отоюражения кнопки New Item
    create_new_item = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/view/all/newJob']")))
    assert create_new_item.is_displayed()

@pytest.mark.dependency()
def test_create_new_item(browser):#Проверка ввода имени в поле ввода New Item
    create_new_item = browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']")
    create_new_item.click()
    item_name_fild = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='name']")))
    item_name_fild.send_keys('London')
    folder_type = browser.find_element(By.XPATH,"//span[text()='Folder']")
    folder_type.click()
    assert item_name_fild.get_attribute('value') == 'London'
    button_OK = browser.find_element(By.XPATH,"//button[@id='ok-button']")
    button_OK.click()
    assert browser.current_url == f'http://localhost:8080/job/London/configure'


@pytest.mark.dependency(depends=["test_create_new_item"])
def test_open_configuration(browser):
    WebDriverWait(browser,2)
    assert browser.current_url == f'http://localhost:8080/job/London/configure'

@pytest.mark.dependency(depends=["test_open_configuration"])
def test_display_name(browser):
    display_name_filed = browser.find_element(By.XPATH,"//input[@type='text']")
    display_name_filed.send_keys('New York')
    assert display_name_filed.get_attribute('value') == 'New York'

@pytest.mark.dependency(depends=["test_display_name"])
def test_input_description(browser):
    description_filed =  WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@name='_.description']")))
    description_filed.send_keys('Some text...')
    assert description_filed.get_attribute('value') == 'Some text...'