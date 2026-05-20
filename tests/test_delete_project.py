import random
import string

import pytest
from selenium.common import TimeoutException

from pages.home_page import HomePage

def generate_project_name():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))

current_project_name = generate_project_name()

@pytest.mark.dependency()
def test_cancel_delete_job(browser):

    result_project_name = (HomePage(browser)
     .click_new_item()
     .set_project_name(current_project_name)
     .select_pipeline_and_ok_click()
     .click_save()
     .click_delete()
     .refresh_page()
     .get_project_name())

    assert result_project_name == current_project_name

@pytest.mark.dependency(depends=["test_cancel_delete_job"])
def test_delete_job(browser):
    result = True

    try:
        (HomePage(browser)
         .click_pipeline_job(current_project_name)
         .click_delete()
         .click_confirm_delete_button()
         .click_pipeline_job(current_project_name))

    except TimeoutException:
        result = False

    assert result == False


