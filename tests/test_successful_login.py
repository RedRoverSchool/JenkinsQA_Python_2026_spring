from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def test_successful_login(browser):
    actions = ActionChains(browser)
    menu_item = browser.find_element(By.ID, "root-action-UserAction")
    actions.move_to_element(menu_item).perform()
    browser.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()

    browser.find_element(By.CSS_SELECTOR, "#j_username").send_keys("admin")


    browser.find_element(By.CSS_SELECTOR, "#j_password").send_keys("admin")
    password_input.

    browser.find_element(By.XPATH, "//button[@type='submit']").click()


    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")

    assert "Welcome to Jenkins!" in label.text



























