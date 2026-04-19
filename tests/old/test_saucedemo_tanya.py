from selenium.webdriver.common.by import By


def test_login(browser):
    browser.get("https://www.saucedemo.com/")

    login_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
    login_button = browser.find_element(By.XPATH, '//*[@id="login-button"]')

    login_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')
    login_button.click()

    assert 'inventory' in browser.current_url





