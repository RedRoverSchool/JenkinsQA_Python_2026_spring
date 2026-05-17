import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage

MULTICONFIGURATION_PROJECT_NAME = "MultiConfigName"

@pytest.mark.dependency()
def test_create_multi_configuration_project(browser):
    multi_configuration_project_name = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .select_multiconfiguration_project_and_ok_click()
        .click_save()
        .go_home_page()
        .get_project_name()
    )

    assert multi_configuration_project_name == MULTICONFIGURATION_PROJECT_NAME

@pytest.mark.dependency(depends=["test_create_multi_configuration_project"])
def test_create_project_with_exist_name(browser):
    error_message_text = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .select_multiconfiguration_project()
        .get_unsafe_character_and_existed_name_error_message()
    )

    assert error_message_text == f"» A job already exists with the name ‘{MULTICONFIGURATION_PROJECT_NAME}’"

def test_verify_status_switching_enable_button(browser):
    disable_project_message = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .select_multiconfiguration_project_and_ok_click()
        .click_enable_toggle()
        .click_save_button()
        .get_disable_project_message()
    )

    assert "This project is currently disabled" in disable_project_message

def test_verify_enable_toggle_has_tooltip(browser):
    toggle_tooltip = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .select_multiconfiguration_project_and_ok_click()
        .get_text_toggle_tooltip()
    )

    assert toggle_tooltip == "Enable or disable the current project"

@pytest.mark.parametrize("special_characters ",[
    "!", "%", "&", "#", "@", "*", "?", "^", "|", "/", "]", "["
])
def test_create_item_with_special_characters(browser, special_characters):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(f"{MULTICONFIGURATION_PROJECT_NAME}{special_characters}")
    browser.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()

    error_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "itemname-invalid"))).text

    expected_error_message = f"‘{special_characters}’ is an unsafe character"
    assert error_message == "» " + f"‘{special_characters}’ is an unsafe character"

    browser.find_element(By.ID, "ok-button").click()
    assert browser.find_element(By.TAG_NAME, "p").text == expected_error_message

@pytest.mark.dependency(depends=["test_create_multi_configuration_project"])
def test_search_created_project(browser):
    browser.find_element(By.ID, "root-action-SearchAction").click()

    browser.find_element(By.ID, "command-bar").send_keys(MULTICONFIGURATION_PROJECT_NAME)

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//a[contains(@href, '/job/{MULTICONFIGURATION_PROJECT_NAME}/')]"))).click()

    WebDriverWait(browser, 10).until(
        EC.url_contains(f"/job/{MULTICONFIGURATION_PROJECT_NAME}/"))

    assert WebDriverWait(browser, 10).until(
         EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text == MULTICONFIGURATION_PROJECT_NAME

@pytest.mark.skip
@pytest.mark.dependency(depends=["test_create_multi_configuration_project"])
def test_check_delete_view_on_dashboard(browser):
    view_name = "NewView"

    browser.find_element(By.CLASS_NAME, "addTab").click()
    browser.find_element(By.ID, "name").send_keys(view_name)
    browser.find_element(By.CSS_SELECTOR, "label[for='hudson.model.MyView']").click()
    browser.find_element(By.ID, "ok").click()

    browser.find_element(By.CSS_SELECTOR, "a[data-title='Delete View']").click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-id='ok']"))).click()

    view_panel_elements = WebDriverWait(browser, 10).until(
         EC.visibility_of_element_located((By.CLASS_NAME, "tabBarFrame"))).text

    assert view_name not in view_panel_elements
