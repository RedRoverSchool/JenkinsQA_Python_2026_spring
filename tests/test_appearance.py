import pytest

from pages.home_page import HomePage


@pytest.mark.parametrize("themes", ["none", "dark", "dark-system"])
def test_appearance_theme(browser, themes):

    theme = (
        HomePage(browser)
             .click_manage_gear()
             .click_appearance()
             .set_theme(themes)
             .click_apply_button()
             .get_theme()
    )

    assert themes == theme


def test_appearance_show_pipeline_stages(browser):
    stages = (HomePage(browser)
              .click_manage_gear()
              .click_appearance()
              .select_checkbox_show_pipeline_stages_on_job_page()
              .click_apply_button()
              .go_home_page()
              .click_new_item()
              .set_project_name("appearance show")
              .select_pipeline_and_ok_click()
              .go_home_page()
              .click_pipeline_job("appearance show")
              .is_display_stages()
    )

    assert stages
