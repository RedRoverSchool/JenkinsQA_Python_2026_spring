from selenium.webdriver.common.by import By

def test_create_new_item_folder(browser):
    browser.find_element(By.CLASS_NAME, 'task-link').click()
    browser.find_element(By.ID, 'name').send_keys("New item")
    browser.find_element(By.CLASS_NAME, 'com_cloudbees_hudson_plugins_folder_Folder').click()
    browser.find_element(By.ID, 'ok-button').click()

    browser.find_element(By.XPATH, '//*[@id="bottom-sticker"]/div/button[1]').click()
    browser.find_element(By.XPATH, '//*[@id="page-header"]/div[1]/div/a').click()

    new_item = browser.find_element(By.XPATH, '//*[@id="job_New item"]/td[3]/a/span').text

    assert new_item == "New item"