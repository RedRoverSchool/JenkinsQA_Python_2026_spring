import pytest
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
    error_message = (
        HomePage(browser)
        .click_new_item()
        .set_project_name(MULTICONFIGURATION_PROJECT_NAME+special_characters)
        .select_multiconfiguration_project_and_ok_click()
        .get_unsafe_character_error_message()
    )

    assert error_message == f"‘{special_characters}’ is an unsafe character"

@pytest.mark.dependency(depends=["test_create_multi_configuration_project"])
def test_search_created_project(browser):
    created_project_name = (
        HomePage(browser)
        .click_search_icon()
        .set_created_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .click_searched_project_name(MULTICONFIGURATION_PROJECT_NAME)
        .get_project_name()
    )

    assert created_project_name == MULTICONFIGURATION_PROJECT_NAME

@pytest.mark.dependency(depends=["test_create_multi_configuration_project"])
def test_check_delete_view_on_dashboard(browser):
    view_name = "NewView"

    view_panel_elements = (
        HomePage(browser)
        .click_new_view_link()
        .set_new_view_name(view_name)
        .check_my_view_radio_btn()
        .click_create_btn()
        .delete_user_view()
        .get_view_panel_elements()
    )

    assert view_name not in view_panel_elements

def test_search_project_from_several_created_project(browser):
    multiconfig_projects = [
        "FirstMultiConfig",
        "SecondMultiConfig",
        "ThirdMultiConfig",
        "ForthMultiConfig"
    ]
    created_project_list = []

    for project_name in multiconfig_projects:
        multiconfig_project = (
            HomePage(browser)
            .click_new_item()
            .set_project_name(project_name)
            .select_multiconfiguration_project_and_ok_click()
            .click_save()
            .go_home_page()
        )

        created_project_name = multiconfig_project.get_created_project_name(project_name)
        assert created_project_name == project_name
        created_project_list.append(created_project_name)

    assert len(created_project_list) == len(multiconfig_projects)

    project_list_name = (
        HomePage(browser)
        .click_search_icon()
        .set_created_project_name(multiconfig_projects[1])
        .click_searched_project_name(multiconfig_projects[1])
        .get_project_name()
    )

    assert project_list_name == multiconfig_projects[1]
