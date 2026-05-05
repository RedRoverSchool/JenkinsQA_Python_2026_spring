import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


job_name = "My_test"

@pytest.mark.dependency()
def test_build_steps_field_is_available(browser):

    browser.find_element(By.XPATH, '//*[@id="tasks"]//a').click()
    input_name = browser.find_element(By.ID, "name")
    input_name.send_keys(job_name)
    browser.find_element(By.CLASS_NAME, 'hudson_model_FreeStyleProject').click()
    browser.find_element(By.XPATH, '//*[@id="ok-button"]').click()
    field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "build-steps"))
    )

    assert field is not None



@pytest.mark.dependency(depends=["test_build_steps_option_is_available"])
def test_build_steps_execute_shell_option(browser):

    script_for_linux = '''echo "Starting process..."
    echo "Hostname: $(hostname)"
    echo "Current User: $(whoami)" 
    echo "Uptime: $(uptime -p)"
    sleep 1
    echo "1 seconds have passed. Continuing..." '''

    xpath = f"//*[@id='job_{job_name}']/td[3]/a"
    browser.find_element(By.XPATH, xpath).click()
    browser.find_element(By.XPATH, "//a[contains(., 'Configure')]").click()

    add_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@suffix='builder']"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)

    add_button.click()

    browser.find_element(By.XPATH, "//button[normalize-space()='Execute shell']").click()

    editor = browser.find_element(By.CSS_SELECTOR, ".CodeMirror")
    ActionChains(browser).move_to_element(editor).click().send_keys(script_for_linux).perform()

    browser.find_element(By.XPATH, '//*[@id="bottom-sticker"]/div/button[1]').click()
    browser.find_element(By.XPATH, "//a[.//span[normalize-space()='Build Now']]").click()
    browser.find_element(By.XPATH, '//a[@href="/job/My_test/1/console"]').click()

    log = browser.find_element(By.ID, "out").text

    assert "Finished: SUCCESS" in log
