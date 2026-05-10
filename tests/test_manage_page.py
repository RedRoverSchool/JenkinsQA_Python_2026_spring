import pytest
import pytest_dependency
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def create_freestyle_project_with_timer(browser, name_project: str, command_shell: str):
    wait = WebDriverWait(browser, 5)

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()
    browser.find_element(By.ID, "name").send_keys(name_project)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Freestyle project']"))).click()
    browser.find_element(By.XPATH, '//*[@id="ok-button"]').click()

    button_add_build_step = browser.find_element(By.XPATH, "//button[text()='Add build step']")
    browser.execute_script("arguments[0].scrollIntoView(true);", button_add_build_step)
    button_add_build_step.click()

    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "jenkins-dropdown__item")))
    browser.find_element(By.XPATH, "//button[normalize-space()='Execute shell']").click()

    ActionChains(browser)\
        .move_to_element(browser.find_element(By.XPATH, "//div[contains(@class, 'cm-s-default')]"))\
        .click().send_keys(command_shell).perform()

    browser.find_element(By.NAME, "Submit").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='Permalinks']")))
    browser.find_element(By.CLASS_NAME, "app-jenkins-logo").click()


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

    item_name = "job"
    count_jobs = range(1, 4)
    for i in count_jobs:
        create_freestyle_project_with_timer(browser, item_name + str(i), "sleep 60")

    for _ in range(2):
        for i in count_jobs:
            browser.find_element(By.XPATH, f"//tr/td[7]//a[@tooltip='Schedule a Build for {item_name}{i}']").click()

    list_items = browser.find_elements(By.XPATH, f"//div[@class='pane-content']//tr/td/a[contains(text(),'{item_name}')]")
    list_items = [item.text for item in list_items]
    target_item = [f"{item_name}{i}" for i in count_jobs]

    assert all(item in list_items for item in target_item)


@pytest.mark.dependency()
def test_build_history_display_status(browser: selenium.webdriver.chrome.webdriver.WebDriver):
    name_jobs = ['job4', 'job5', 'job6']

    for name in name_jobs:
        create_freestyle_project_with_timer(browser, name, "echo $EXECUTOR_NUMBER\npwd\nls -lsa /")
        browser.find_element(By.XPATH, f"//tr/td[7]//a[@tooltip='Schedule a Build for {name}']").click()

    browser.find_element(By.XPATH, "//a[@href='/view/all/builds']").click()
    job_color_status = browser.find_elements(By.XPATH, "//tbody/tr/td[contains(@class, 'jenkins-table__icon')]/div")[0].get_attribute('innerHTML')
    name_job = browser.find_element(By.XPATH, "//tbody/tr/td/a[@class='jenkins-table__link model-link']").get_attribute("href")
    timer_job = browser.find_elements(By.XPATH, "//tbody/tr/td[@data]")
    status_job = browser.find_elements(By.XPATH, "//tbody/tr/td[4]")

    assert 'id="blue"' in job_color_status or 'id="red"' in job_color_status, "нет джобы с успешным статусом выполнения"
    assert any(job in name_job for job in name_jobs), "ни одна тестовая джоба не была запущена на выполнение"
    assert any("sec" in timer.text for timer in timer_job), "ни у одной джобы нет прошедшего времени выполнения"
    assert any("stable" in status.text for status in status_job), "нет джобы с успешным статусом выполнения"


@pytest.mark.dependency(depends=["test_build_history_display_status"])
def test_build_history_console_output(browser: selenium.webdriver.chrome.webdriver.WebDriver):
    browser.find_element(By.XPATH, "//a[@href='/view/all/builds']").click()
    browser.find_element(By.XPATH, "//tbody/tr/td[@class='jenkins-table__cell--tight']").click()
    h1 = browser.find_element(By.XPATH, "//h1").text
    print(f"{h1=}")
    assert "Console" in h1


def create_freestyle_project_with_timer(browser, name_project: str, command_shell: str):
    wait = WebDriverWait(browser, 5)

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href='/view/all/newJob']"))).click()
    browser.find_element(By.ID, "name").send_keys(name_project)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Freestyle project']"))).click()
    browser.find_element(By.XPATH, '//*[@id="ok-button"]').click()

    button_add_build_step = browser.find_element(By.XPATH, "//button[text()='Add build step']")
    browser.execute_script("arguments[0].scrollIntoView(true);", button_add_build_step)
    button_add_build_step.click()

    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "jenkins-dropdown__item")))
    browser.find_element(By.XPATH, "//button[normalize-space()='Execute shell']").click()

    ActionChains(browser)\
        .move_to_element(browser.find_element(By.XPATH, "//div[contains(@class, 'cm-s-default')]"))\
        .click().send_keys(command_shell).perform()

    browser.find_element(By.NAME, "Submit").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[text()='Permalinks']")))
    browser.find_element(By.CLASS_NAME, "app-jenkins-logo").click()
