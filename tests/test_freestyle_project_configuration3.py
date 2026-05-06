import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

JOB_NAME = "Test_project"

def wait_until_clickable(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )

@pytest.mark.dependency()
def test_build_steps_field_is_available(browser):
    browser.find_element(By.XPATH, '//*[@id="tasks"]//a').click()
    input_name = browser.find_element(By.ID, "name")
    input_name.send_keys(JOB_NAME)
    browser.find_element(By.CLASS_NAME, 'hudson_model_FreeStyleProject').click()
    browser.find_element(By.XPATH, '//*[@id="ok-button"]').click()
    field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "build-steps"))
    )

    assert field is not None


@pytest.mark.dependency(depends=["test_build_steps_field_is_available"])
def test_build_steps_configure_shell_option(browser):

    script_for_linux = '''echo "Starting process..."
    echo "Hostname: $(hostname)"'''

    xpath = f"//*[@id='job_{JOB_NAME}']/td[3]/a"
    browser.find_element(By.XPATH, xpath).click()
    browser.find_element(By.XPATH, "//a[contains(., 'Configure')]").click()

    add_button = wait_until_clickable(browser, (By.XPATH, "//button[@suffix='builder']"))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
    add_button.click()
    browser.find_element(By.XPATH, "//button[normalize-space()='Execute shell']").click()

    editor = browser.find_element(By.CSS_SELECTOR, ".CodeMirror")
    ActionChains(browser).move_to_element(editor).click().send_keys(script_for_linux).perform()
    browser.find_element(By.XPATH, '//*[@id="bottom-sticker"]/div/button[1]').click()

    header = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text

    assert header == JOB_NAME