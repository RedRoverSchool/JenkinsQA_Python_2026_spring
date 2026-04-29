from selenium.webdriver.common.by import By


def test_add_description_folder(browser):
    description_text = "Folder Description test"

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys("Folder_Name")
    browser.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.find_element(By.CSS_SELECTOR, "textarea[name='_.description']").send_keys(description_text)
    browser.find_element(By.NAME, "Submit").click()

    assert browser.find_element(By.ID, "view-message").text == description_text
