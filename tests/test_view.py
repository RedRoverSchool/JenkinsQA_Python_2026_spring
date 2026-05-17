from pages.home_page import HomePage

def test_create_new_view(browser):
    new_view_name = "New_view"

    view_names_list = (
        HomePage(browser)
        .click_new_item()
        .set_project_name("pipe_line_project")
        .select_pipeline_and_ok_click()
        .click_submit_button()
        .go_home_page()
        .click_new_view_link()
        .set_new_view_name(new_view_name)
        .check_my_view_radio_btn()
        .click_create_btn()
        .go_home_page()
        .get_view_names_list()
    )

    assert new_view_name in view_names_list

