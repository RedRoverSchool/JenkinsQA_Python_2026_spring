import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage

FOLDER_NAME = "TestFolder"
SECOND_FOLDER_NAME = "SecondFolder"
FOLDER_DESCRIPTION = "Folder description"


def create_folder(driver, name, full_creation=True):
    wait5 = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH, "//a[contains(@href, '/newJob')]").click()
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.CLASS_NAME, "com_cloudbees_hudson_plugins_folder_Folder").click()
    wait5.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    if full_creation:
        wait5.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()


@pytest.mark.dependency()
def test_create_folder(browser):
    project_names_list = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .save_click()
        .go_home_page()
        .get_project_names_list()
    )

    assert len(project_names_list) > 0
    assert project_names_list[0] == FOLDER_NAME


def test_create_folder_with_display_name(browser):
    display_name = "Display_Folder"

    folder_name = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .set_display_name(display_name)
        .save_click()
        .get_project_name()
    )

    assert folder_name == display_name


def test_create_folder_with_description(browser):
    description_text = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .set_description(FOLDER_DESCRIPTION)
        .save_click()
        .get_config_description()
    )

    assert description_text == FOLDER_DESCRIPTION


@pytest.mark.dependency(depends=["test_create_folder"])
def test_create_nested_folder(browser):
    nested_folder_page = (
        HomePage(browser)
        .click_project_name(FOLDER_NAME, job_type="folder")
        .new_item_click()
        .set_project_name(SECOND_FOLDER_NAME)
        .select_folder_and_ok_click()
        .save_click())

    assert nested_folder_page.get_full_folder_name() == f"Full folder name: {FOLDER_NAME}/{SECOND_FOLDER_NAME}"
    assert nested_folder_page.get_breadcrumb_texts_list() == [FOLDER_NAME, SECOND_FOLDER_NAME]


def test_create_folder_with_empty_name_negative(browser):
    error_message = (
        HomePage(browser)
        .new_item_click()
        .select_folder()
        .get_empty_name_error_message()
    )

    assert error_message == "» This field cannot be empty, please enter a valid name"


@pytest.mark.parametrize("character", ["/", "\\", "|", "?", "*", ":", ">", "<"])
def test_create_folder_with_invalid_characters_negative(browser, character):
    error_message = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(FOLDER_NAME+character)
        .select_folder()
        .get_unsafe_character_and_existed_name_error_message()
    )

    assert error_message == f"» ‘{character}’ is an unsafe character"


@pytest.mark.dependency(depends=["test_create_folder"])
def test_create_folder_with_duplicate_name_in_same_parent_negative(browser):
    error_message = (
        HomePage(browser)
        .new_item_click()
        .set_project_name(FOLDER_NAME)
        .select_folder()
        .get_unsafe_character_and_existed_name_error_message()
    )

    assert error_message == f"» A job already exists with the name ‘{FOLDER_NAME}’"


@pytest.mark.dependency(depends=["test_create_nested_folder"])
def test_create_folder_with_same_name_in_different_parent(browser):
    create_folder(browser, SECOND_FOLDER_NAME)

    assert browser.find_element(By.CLASS_NAME, "job-index-headline").text == SECOND_FOLDER_NAME


@pytest.mark.dependency(depends=['test_create_folder'])
def test_create_folder_from_copy(browser):
    wait = WebDriverWait(browser, 5)

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "New Item"))).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, 'name'))).send_keys('Folder from copy')

    wait.until(
        EC.element_to_be_clickable((By.ID, 'from'))).send_keys('TestFolder')

    wait.until(
        EC.element_to_be_clickable((By.ID, 'from'))).send_keys(Keys.ENTER)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@value="Save"]'))).click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//h1[text()="Folder from copy"]')))

    wait.until(
        EC.presence_of_element_located((By.ID, 'jenkins-head-icon')))

    wait.until(
        EC.element_to_be_clickable((By.ID, 'jenkins-head-icon'))).click()

    new_folder = wait.until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Folder from copy')))
    assert new_folder.text == 'Folder from copy'

@pytest.mark.skip
def test_add_description_after_creation(browser):
    description_content = (
            HomePage(browser)
            .new_item_click()
            .set_project_name(FOLDER_NAME)
            .select_folder_and_ok_click()
            .save_click()
            .click_add_description_link()
            .add_description(FOLDER_DESCRIPTION)
            .get_description()
    )

    assert description_content == FOLDER_DESCRIPTION
