from selenium.webdriver.common.by import By


def test_empty_item_name(browser):
    element_button = browser.find_element(By.XPATH, '//a[contains(., "New Item")]')
    element_button.click()
    assert "/view/all/newJob" in browser.current_url
    element_input = browser.find_element(By.ID,"name")

    folder = browser.find_element(By.XPATH,"//li[contains(@class, 'folder_Folder')]")
    folder.click()
    ok_button = browser.find_element(By.ID,"ok-button")
    warning_message = browser.find_element(By.XPATH,"//div[@id='itemname-required']")

    assert element_input.get_attribute("value") == ""
    assert warning_message.is_displayed()
    assert warning_message.text.strip() == "» This field cannot be empty, please enter a valid name"
    assert not ok_button.is_enabled()