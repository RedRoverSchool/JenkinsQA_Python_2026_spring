import pytest

from pages.home_page import HomePage

@pytest.mark.skip
def test_navigation_to_tools(browser):
    text = "Configure tools, their locations and automatic installers."

    description_on_the_page = (HomePage(browser)
                               .click_manage_gear()
                               .click_tools()
                               .get_page_description())

    assert text in description_on_the_page
    assert f"/manage/configureTools/" in browser.current_url

@pytest.mark.skip
def test_configuration_sections(browser):
    expected_section_titles = ['maven configuration', 'jdk installations', 'git installations', 'gradle installations',
                               'ant installations', 'maven installations']

    actual_section_titles = (HomePage(browser)
                             .click_manage_gear()
                             .click_tools()
                             .get_section_titles())

    assert actual_section_titles == expected_section_titles
