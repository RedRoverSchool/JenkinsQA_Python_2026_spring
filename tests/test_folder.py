import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage

FOLDER_NAME = "TestFolder"
SECOND_FOLDER_NAME = "SecondFolder"
FOLDER_DESCRIPTION = "Folder description"


@pytest.mark.dependency(name="test_create_folder")
def test_create_folder(browser):
    project_names_list = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .click_save()
        .go_home_page()
        .get_project_names_list()
    )

    assert len(project_names_list) > 0
    assert project_names_list[0] == FOLDER_NAME


def test_create_folder_with_display_name(browser):
    display_name = "Display_Folder"

    folder_name = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .set_display_name(display_name)
        .click_save()
        .get_project_name()
    )

    assert folder_name == display_name


def test_create_folder_with_description(browser):
    description_text = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .set_description(FOLDER_DESCRIPTION)
        .click_save("folder")
        .get_config_description()
    )

    assert description_text == FOLDER_DESCRIPTION


@pytest.mark.dependency(depends=["test_create_folder"])
def test_create_nested_folder(browser):
    nested_folder_page = (
        HomePage(browser)
        .click_project_name(FOLDER_NAME, job_type="folder")
        .click_new_item()
        .set_project_name(SECOND_FOLDER_NAME)
        .select_folder_and_ok_click()
        .click_save("folder"))

    assert nested_folder_page.get_full_folder_name() == f"Full folder name: {FOLDER_NAME}/{SECOND_FOLDER_NAME}"
    assert nested_folder_page.get_breadcrumb_texts_list() == [FOLDER_NAME, SECOND_FOLDER_NAME]


def test_create_folder_with_empty_name_negative(browser):
    error_message = (
        HomePage(browser)
        .click_new_item()
        .select_folder()
        .get_empty_name_error_message()
    )

    assert error_message == "» This field cannot be empty, please enter a valid name"


@pytest.mark.parametrize("character", ["/", "\\", "|", "?", "*", ":", ">", "<"])
def test_create_folder_with_invalid_characters_negative(browser, character):
    error_message = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME+character)
        .select_folder()
        .get_unsafe_character_and_existed_name_error_message()
    )

    assert error_message == f"» ‘{character}’ is an unsafe character"


@pytest.mark.dependency(depends=["test_create_folder"])
def test_create_folder_with_duplicate_name_in_same_parent_negative(browser):
    error_message = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder()
        .get_unsafe_character_and_existed_name_error_message()
    )

    assert error_message == f"» A job already exists with the name ‘{FOLDER_NAME}’"


@pytest.mark.dependency(depends=["test_create_nested_folder"])
def test_create_folder_with_same_name_in_different_parent(browser):
    project_names_list = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(SECOND_FOLDER_NAME)
        .select_folder_and_ok_click()
        .click_save()
        .go_home_page()
        .get_project_names_list()
    )

    assert len(project_names_list) > 0
    assert SECOND_FOLDER_NAME in project_names_list


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
        .click_new_item()
        .set_project_name(FOLDER_NAME)
        .select_folder_and_ok_click()
        .click_save()
        .click_add_description_link()
        .add_description(FOLDER_DESCRIPTION)
        .get_description()
    )

    assert description_content == FOLDER_DESCRIPTION

@pytest.mark.dependency(depends=['test_create_folder'])
def test_folder_apply_button(browser):
    apply_result = (
        HomePage(browser)
        .click_project_name(FOLDER_NAME, 'folder')
        .click_project_configure('folder')
        .set_display_name("Display_name")
        .click_apply()
        .get_notification_saved()
    )

    assert apply_result == "Saved"
    assert "configure" in browser.current_url, "User was redirected from the configuration page after clicking Apply"

@pytest.mark.dependency(depends=['test_folder_apply_button'])
def test_folder_save_button(browser):
    save_result = (HomePage(browser)
        .click_project_name(FOLDER_NAME, 'folder')
        .click_project_configure('folder')
        .set_display_name("Display_name")
        .click_save('folder')
    )

    assert "configure" not in browser.current_url, "Error: Save button failed to redirect the user to the Folder's main page!"
