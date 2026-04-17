from selenium.webdriver.common.by import By

def test_form(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    browser.implicitly_wait(5)

    text_box = browser.find_element(By.NAME, "my-password")
    text_box.send_keys("admin")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button")
    submit_button.click()

    message = browser.find_element(By.ID, "message")
    assert "Received!" in message.text