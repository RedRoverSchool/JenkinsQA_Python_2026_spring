import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sign_out(browser):
    wait = WebDriverWait(browser, 10)

    user_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root-action-UserAction")))
    actions = ActionChains(browser)
    actions.move_to_element(user_icon).perform()

    wait = WebDriverWait(browser, 10)

    sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/logout')]")))
    sign_out_button.click()

    time.sleep(2)

    username_field = wait.until(EC.presence_of_element_located((By.ID, "j_username")))
    password_field = browser.find_element(By.ID, "j_password")

    assert username_field.get_attribute("value") == ""
    assert password_field.get_attribute("value") == ""






