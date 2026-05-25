from pages.home_page import HomePage
from pages.base_page import BasePage
import pytest

NAME = "test-pipeline"

@pytest.mark.dependency()
def test_create_multibranch_pipeline(browser):
    result = ((HomePage(browser))
              .click_new_item()
              .set_project_name("test-pipeline")
              .select_multibranch_scroll_and_ok_click()
              .click_save())

    assert result.get_project_name() == NAME

@pytest.mark.dependency(depends=["test_create_multibranch_pipeline"])
def test_redirect_multibranch_pipeline_from_dashboard(browser):
    result = (HomePage(browser)
              .click_project_name(f"{NAME}")
              .get_project_name())

    assert result == NAME



def test_delete_multibranch_pipeline_from_sidepanel(browser):
    test_create_multibranch_pipeline(browser)
    ((BasePage(browser))
    .go_home_page()
        .click_project_name(f"{NAME}")
            .click_delete()
                .click_cancel_delete_button()
                    .click_delete()
                        .click_confirm_delete_button())

    assert HomePage(browser).is_project_disappeared(NAME)




def test_delete_multibranch_pipeline_from_dashboard(browser):
    test_create_multibranch_pipeline(browser)
    ((HomePage(browser))
    .go_home_page()
        .open_project_dropdown(f"{NAME}")
            .click_delete_project_in_dropdown_menu(NAME)
                .click_cancel_delete_button_homepage()
                    .open_project_dropdown(f"{NAME}")
                        .click_delete_project_in_dropdown_menu(NAME)
                            .click_confirm_delete_button_homepage())

    assert HomePage(browser).is_project_disappeared(NAME)











