from pages.base_page import BasePage
from pages.about_jenkins_page import AboutJenkinsPage

def test_footer_jenkins_version(browser):

    version = BasePage(browser).get_jenkins_version()

    assert version == "Jenkins 2.541.3"


def test_about_jenkins(browser):

    BasePage(browser).click_jenkins_version_button().click_about_jenkins()
    about_page = AboutJenkinsPage(browser)

    assert "About Jenkins - Manage Jenkins - Jenkins" in about_page.get_page_title()
    assert "/manage/about/" in about_page.get_page_url()
    assert about_page.get_title_text() == "Jenkins"
    assert about_page.get_version_text() == "Version 2.541.3"
    assert about_page.get_table_rows_count() > 0
    assert about_page.is_jenkins_core_present(), "Jenkins core не найдено"
