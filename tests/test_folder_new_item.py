from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_folder_new_item(browser):
    """Тест доступности кнопки ОК при создании New Item"""
    new_item = browser.find_element(By.CSS_SELECTOR, ".task-link.task-link-no-confirm ")
    new_item.click()
    item_name_field = browser.find_element(By.ID, "name")
    item_name_field.send_keys("TestNew")
    folder_radio = browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder")
    folder_radio.click()

    buttom = browser.find_element(By.ID, "ok-button")

    assert buttom.is_enabled()