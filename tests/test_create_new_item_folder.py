from selenium.webdriver.common.by import By

folder_name = "Folder at"

def test_create_new_item_folder(browser):

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(folder_name)
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.NAME, "Submit").click()

    folder_name_created = browser.find_element(By.CLASS_NAME, "job-index-headline").text
    assert folder_name_created == folder_name
