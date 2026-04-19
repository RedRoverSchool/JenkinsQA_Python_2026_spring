from selenium.webdriver.common.by import By

USERNAME = (By.XPATH, '//input[@name="username"]')
PASSWORD = (By.XPATH, '//input[@name="password"]')
BUTTON = (By.XPATH, "//input[@value='Log In']")


def test_input_admin(browser):
    """Негативный тест логина в админ-панель"""
    browser.implicitly_wait(2)   # это общее ожидание для всех browser.find_element()
    browser.get("https://parabank.parasoft.com/parabank/admin.htm")

    text_box1 = browser.find_element(*USERNAME)
    text_box2 = browser.find_element(*PASSWORD)
    submit_button = browser.find_element(*BUTTON)

    text_box1.send_keys("Selenium")
    text_box2.send_keys("Test")
    submit_button.click()

    element_text = browser.find_element(By.CSS_SELECTOR, "#rightPanel > p").text

    assert "could not be verified" in element_text