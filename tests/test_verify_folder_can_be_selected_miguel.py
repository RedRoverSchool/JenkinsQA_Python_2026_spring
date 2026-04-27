from selenium.webdriver.common.by import By


def test_verify_folder_selected(browser):
    new_item_button = browser.find_element(By.XPATH, "//a[contains(., 'New Item')]")
    new_item_button.click()
    assert "/view/all/newJob" in browser.current_url
    folder = browser.find_element(By.XPATH, "//li[contains(@class,'folder_Folder')]")
    folder.click()
    assert "active"  in folder.get_attribute("class")
