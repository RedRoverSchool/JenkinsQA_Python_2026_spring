from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.home_page import HomePage


def test_verify_navigation_to_manage_page(browser):
    wait = WebDriverWait(browser, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction"))).click()

    wait.until(EC.url_contains("/manage"))

    assert "/manage" in browser.current_url


def test_verify_icon_is_visible(browser):
    wait = WebDriverWait(browser, 10)

    assert wait.until(EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction"))).is_displayed()


def test_verify_tooltip_text_and_clickability(browser):

    home_page = HomePage(browser)
    home_page.hover_to_manage_gear()

    assert home_page.get_cursor_type() == "pointer"
    assert home_page.get_manage_gear_tooltip_text() == "Manage Jenkins"

    manage_page = home_page.click_manage_gear()

    assert manage_page.check_appearance_visibility()


def test_build_queue_visibility(browser):

    item_name = ["job1", "job2", "job3"]

    for job_name in item_name:
        (HomePage(browser)
         .click_new_item()
         .set_project_name(job_name)
         .select_freestyle_and_ok_click()
         .button_add_build_step_click()
         .select_execute_shell_option()
         .set_shell_script("echo $EXECUTOR_NUMBER\npwd\nls -lsa /\nsleep 60")
         .click_save()
         .go_home_page()
         .click_schedule_build(job_name))

    list_jobs_name = HomePage(browser).get_names_jobs_list_build_queue()

    assert any(job_name in item_name for job_name in list_jobs_name)
