from pages.home_page import HomePage
from pages.base_page import BasePage
import pytest

NAME = "test-pipeline"

@pytest.mark.dependency()
def test_create(browser):
    result = ((HomePage(browser))
              .click_new_item()
              .set_project_name("test-pipeline")
              .select_multibranch_scroll_and_ok_click()
              .click_save())

    assert result.get_project_name() == NAME

@pytest.mark.dependency(depends=["test_create"])
def test_redirect_multibranch_pipeline_from_dashboard(browser):
    result = (BasePage(browser)
              .go_home_page()
              .click_project_name(f"{NAME}")
              .get_project_name())

    assert result == NAME








