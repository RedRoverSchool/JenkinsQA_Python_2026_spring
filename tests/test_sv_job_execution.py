from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_create_and_run_freestyle_job(browser):
    """Тест создаёт New Item (новую джобу) Freestyle project,
    добавляет простой bash-скрипт, запускает в Дженкинсе и проверяет логи"""

    script_for_linux = '''echo "Starting process..."
    echo "Hostname: $(hostname)"
    echo "Current User: $(whoami)" 
    echo "Uptime: $(uptime -p)"
    sleep 1
    echo "1 seconds have passed. Continuing..." '''

    browser.find_element(By.XPATH, '//*[@id="tasks"]/div[1]/span/a').click()
    input_name = browser.find_element(By.ID, "name")
    input_name.send_keys("My_test")
    browser.find_element(By.XPATH, '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]').click()
    browser.find_element(By.XPATH, '//*[@id="ok-button"]').click()

    add_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@suffix='builder']"))
    )

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
    add_button.click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Execute shell']")
        )
    ).click()

    editor = browser.find_element(By.CSS_SELECTOR, ".CodeMirror")
    ActionChains(browser).move_to_element(editor).click().send_keys(script_for_linux).perform()

    browser.find_element(By.XPATH, '//*[@id="bottom-sticker"]/div/button[1]').click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[.//span[normalize-space()='Build Now']]")
        )
    ).click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[@href="/job/My_test/1/console"]')
        )
    ).click()

    log = browser.find_element(By.ID, "out").text

    assert "Finished: SUCCESS" in log

