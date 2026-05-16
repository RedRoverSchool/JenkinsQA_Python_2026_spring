
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage

MULTICONFIGURATION_PROJECT_NAME = "MultiConfigName"

def create_multi_configuration_project(browser, name):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys(name)
    browser.find_element(By.CLASS_NAME, "hudson_matrix_MatrixProject").click()
    browser.find_element(By.ID, "ok-button").click()

    browser.execute_script("""
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    """)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    browser.execute_script("""
                    var logo = document.querySelector('.jenkins-mobile-hide');
                    if (logo) logo.click();
                """)
@pytest.mark.skip
@pytest.mark.dependency()
def test_create_multi_configuration_project(browser):
    multi_configuration_project_name = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .select_multiconfiguration_project_and_ok_click()
        .save_button_click()
        .go_home_page()
        .get_project_name(MULTICONFIGURATION_PROJECT_NAME)
    )

    assert multi_configuration_project_name == MULTICONFIGURATION_PROJECT_NAME

@pytest.mark.skip
def test_verify_status_switching_enable_button(browser):
    create_multi_configuration_project(browser, MULTICONFIGURATION_PROJECT_NAME)
    browser.find_element(By.CSS_SELECTOR, ".jenkins-table__link >span:first-child").click()

    browser.find_element(By.XPATH, "//a[@href='/job/" + MULTICONFIGURATION_PROJECT_NAME + "/configure']").click()
    browser.find_element(By.CSS_SELECTOR, "#toggle-switch-enable-disable-project > label").click()

    browser.execute_script("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        """)
    browser.find_element(By.NAME, "Submit").click()

    actual_disable_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "enable-project"))).text

    assert "This project is currently disabled" in actual_disable_text

@pytest.mark.skip(reason="Flaky test: NoSuchElementException on CI")
def test_verify_enable_toggle_has_tooltip(browser):
    create_multi_configuration_project(browser, MULTICONFIGURATION_PROJECT_NAME)
    browser.find_element(By.CSS_SELECTOR, ".jenkins-table__link >span:first-child").click()
    browser.find_element(By.XPATH, "//a[@href='/job/" + MULTICONFIGURATION_PROJECT_NAME + "/configure']").click()

    enabled_toogle = browser.find_element(By.ID, "toggle-switch-enable-disable-project")

    actions = ActionChains(browser)
    actions.move_to_element(enabled_toogle).perform()

    toggle_tooltip = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "tippy-content"))).text

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

@pytest.mark.skip
@pytest.mark.dependency(depends=["test_create_multi_configuration_project"])
def test_create_project_with_exist_name(browser):
    browser.find_element(By.XPATH, "//a[contains(@href, '/newJob')]").click()
    browser.find_element(By.ID, "name").send_keys(MULTICONFIGURATION_PROJECT_NAME)

    error_message = WebDriverWait(browser, 5).until(
         EC.visibility_of_element_located((By.ID, "itemname-invalid"))).text

    assert error_message == f"» A job already exists with the name ‘{MULTICONFIGURATION_PROJECT_NAME}’"

@pytest.mark.skip
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
