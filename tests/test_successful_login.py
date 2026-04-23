from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_successful_login(browser):
    wait = WebDriverWait(browser, 5)
    user_action = wait.until(
        EC.visibility_of_element_located((By.ID, "root-action-UserAction"))
    )
    ActionChains(browser).move_to_element(user_action).perform()
    logout = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/logout']"))
    )
    logout.click()

    username_input = browser.find_element(By.CSS_SELECTOR, "#j_username")
    username_input.send_keys("admin")

    password_input = browser.find_element(By.CSS_SELECTOR, "#j_password")
    password_input.send_keys("admin")

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    label = browser.find_element(By.XPATH, "//div[@class='empty-state-block']")

    assert "Welcome to Jenkins!" in label.text



























