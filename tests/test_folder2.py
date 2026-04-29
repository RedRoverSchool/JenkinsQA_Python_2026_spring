import pytest
from selenium.webdriver.common.by import By

def open_new_item_page(driver):
    driver.find_element(By.CLASS_NAME, "task-icon-link").click()

def enter_folder_name_and_select(driver, test_folder_name):
    driver.find_element(By.ID, "name").send_keys(test_folder_name)
    driver.find_element(By.XPATH, "//*[@id='j-add-item-type-nested-projects']/ul/li[1]/div[2]").click()

    return test_folder_name

def click_ok(driver):
    driver.find_element(By.ID, "ok-button").click()

def click_jenkins_logo(driver):
    driver.find_element(By.XPATH, "//*[@id='page-header']/div[1]/div/a").click()


def fill_folder_info(driver):
    driver.find_element(By.XPATH, "//*[@id='main-panel']/form/div[1]/div[2]/div/div[2]/input").send_keys("Folder")
    driver.find_element(By.XPATH, "//*[@id='main-panel']/form/div[1]/div[3]/div[2]/textarea").send_keys("Folder")
    driver.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()

    created_folder_name = driver.find_element(By.XPATH, "//*[@id='main-panel']/div[1]/div/h1").text

    click_jenkins_logo(driver)
    dashboard_item = driver.find_element(By.XPATH, "//*[@id='projectstatus']/tbody")

    return created_folder_name, dashboard_item


def check_empty_item_name(driver):
    open_new_item_page(driver)
    driver.find_element(By.XPATH, "//*[@id='j-add-item-type-nested-projects']/ul/li[1]/div[2]").click()
    item_name_tip = driver.find_element(By.ID, "itemname-required").text

    ok_button = driver.find_element(By.ID, "ok-button")
    return item_name_tip, ok_button

def check_existing_item_name(driver, test_folder_name):
    open_new_item_page(driver)

    enter_folder_name_and_select(driver, test_folder_name)

    click_ok(driver)

    fill_folder_info(driver)

    click_jenkins_logo(driver)

    open_new_item_page(driver)

    enter_folder_name_and_select(driver, test_folder_name)

    item_existing_name_error = driver.find_element(By.ID, "itemname-invalid").text


    return test_folder_name, item_existing_name_error

def check_invalid_item_name(driver, test_folder_name):
    open_new_item_page(driver)
    enter_folder_name_and_select(driver, test_folder_name)
    item_invalid_name_error = driver.find_element(By.ID, "itemname-invalid").text

    return test_folder_name, item_invalid_name_error


def test_create_folder_with_valid_name(browser):
    open_new_item_page(browser)
    test_folder_name = enter_folder_name_and_select(browser, "Folder")
    click_ok(browser)
    created_folder_name, dashboard_item = fill_folder_info(browser)

    assert test_folder_name == created_folder_name, "Folder name does not match"
    assert dashboard_item.is_displayed(), "Dashboard is empty"

def test_check_empty_item_name(browser):
    item_name_tip, ok_button = check_empty_item_name(browser)
    assert item_name_tip == "» This field cannot be empty, please enter a valid name", "Item name tip is empty"
    assert ok_button.is_enabled() == False

def test_check_existing_item_name(browser):
    test_folder_name, item_existing_name_error = check_existing_item_name(browser, "Folder")
    assert item_existing_name_error == f"» A job already exists with the name ‘{test_folder_name}’"

@pytest.mark.parametrize("invalid_symbol", [
    "!", "@", "#", "$", "%", "^", "&", "*", "<", ">", ":", ";"
])
def test_check_invalid_item_name(browser, invalid_symbol):
    test_folder_name, item_invalid_name_error = check_invalid_item_name(browser, invalid_symbol)
    assert item_invalid_name_error == f"» ‘{invalid_symbol}’ is an unsafe character"
