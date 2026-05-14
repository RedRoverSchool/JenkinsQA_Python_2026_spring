import random
import string
from conftest import browser
from pages.home_page import HomePage

random_name = "item" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def test_freestyle_project_configuration(browser):
    project_page = (
      HomePage(browser)
     .new_item_click()
     .set_project_name(random_name)
     .select_freestyle_and_ok_click()
     .click_enable_disable_button()
     .button_save_click_2()
    )

    assert "This project is currently disabled" in project_page.get_warning_message(random_name)
    assert project_page.get_status_button().is_displayed()
