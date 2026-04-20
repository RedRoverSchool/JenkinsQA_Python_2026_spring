import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_new_folder(browser):
    wait = WebDriverWait(browser, 5)
    '''Находим кнопку - New item, по которой кликаем'''
    new_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/view/all/newJob']")))
    new_item.click()
    time.sleep(2)

    '''В поле для имени, вводим название папки'''
    input_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="name"]')))
    input_name.send_keys('My first folder')

    '''Кликнуть на карточку - Folder, чтобы выделить'''
    card_folder = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder')))
    card_folder.click()

    '''Кликнуть кнопку - Ок'''
    button_ok = wait.until(EC.element_to_be_clickable((By.ID, 'ok-button')))
    button_ok.click()
    time.sleep(2)

    '''В поле вводим имя в поле Display name'''
    input_display_name = wait.until(EC.visibility_of_element_located((By.NAME, '_.displayNameOrNull')))
    input_display_name.send_keys('My folder')

    '''Вводим имя в поле Description'''
    input_description = wait.until(EC.visibility_of_element_located((By.NAME, '_.description')))
    input_description.send_keys('My description')

    '''Кликаем кнопку - Save'''
    button_save = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@value="Save"]')))
    button_save.click()
    time.sleep(2)

    '''Кликнуть на лого jenkins, чтобы вернуться на стартовую страницу'''
    logo = wait.until(EC.element_to_be_clickable((By.ID, 'jenkins-head-icon')))
    logo.click()
    time.sleep(2)
    folder = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My folder')))
    assert folder.is_displayed()

    time.sleep(2)

