from selenium.webdriver.common.by import By

def locators_storage(browser):
    browser.find_element(By.CLASS_NAME, "task-icon-link").click()

    test_folder_name = "Folder"
    browser.find_element(By.ID, "name").send_keys(test_folder_name)
    browser.find_element(By.XPATH, "//*[@id='j-add-item-type-nested-projects']/ul/li[1]/div[2]").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.XPATH, "//*[@id='main-panel']/form/div[1]/div[2]/div/div[2]/input").send_keys("Folder")
    browser.find_element(By.XPATH, "//*[@id='main-panel']/form/div[1]/div[3]/div[2]/textarea").send_keys("Folder")
    browser.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()

    created_folder_name = browser.find_element(By.XPATH, "//*[@id='main-panel']/div[1]/div/h1").text

    browser.find_element(By.XPATH, "//*[@id='page-header']/div[1]/div/a").click()
    dashboard_item = browser.find_element(By.XPATH, "//*[@id='projectstatus']/tbody")

    return test_folder_name, created_folder_name, dashboard_item


def test_create_folder_with_valid_name(browser):
    test_folder_name, created_folder_name, dashboard_item = locators_storage(browser)

    assert test_folder_name == created_folder_name, "Folder name does not match"
    assert dashboard_item.is_displayed(), "Dashboard is empty"