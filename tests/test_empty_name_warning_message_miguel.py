# ID: TC_01.001.02 | New Item > Creatе a new item > Validate empty item name
#
# Preconditions:
# User is on the New Item page
#
# Description:
#
# Verify that empty item name is not allowed
#
# Steps:
# Open New Item page.
# Leave Item Name field empty.
# Select any item type.
# Observe the validation result.
# Expected Result:
# Warning message that field cannot be empty
# OK button is disabled
# Comments / Notes:
# Observe the validation result.
#
# Acceptance Criteria:
# If the item name field is blank, a warning message appears indicating the name is invalid, and the "OK" button must remain disabled.


from selenium.webdriver.common.by import By

def test_empty_item_mame(browser):
    browser.get("http://localhost:8080/view/all/newJob")
    element = browser.find_element(By.ID,"name")
    assert element.get_attribute("value") == ""
    folder = browser.find_element(By.XPATH,"//li[contains(@class, 'folder_Folder')]")
    folder.click()
    ok_button =browser.find_element(By.ID,"ok-button")
    warning_message = browser.find_element(By.XPATH,"//div[@id='itemname-required']")
    assert warning_message.is_displayed()
    assert not  ok_button.is_enabled()