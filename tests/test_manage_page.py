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


def test_verify_tooltip_and_clickable(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    actions.move_to_element(
        wait.until(
            EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction"))
        )
    ).perform()

    element = wait.until(EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction")))

    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Manage Jenkins')]")))

    cursor = element.value_of_css_property("cursor")

    wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction"))).click()

    assert cursor == "pointer"


def test_build_queue_visibility(browser):

    item_name = ["job1", "job2", "job3"]

    for job_name in item_name:
        (HomePage(browser)
         .new_item_click()
         .set_project_name(job_name)
         .select_freestyle_and_ok_click()
         .button_add_build_step_click()
         .select_option_execute_shell_in_add_build_step_click()
         .set_shell_script("echo $EXECUTOR_NUMBER\npwd\nls -lsa /\nsleep 60")
         .button_save_click()
         .go_home_page()
         .schedule_build_click(job_name))

    list_jobs_name = HomePage(browser).get_names_jobs_list_build_queue()

    assert any(job_name in item_name for job_name in list_jobs_name)
