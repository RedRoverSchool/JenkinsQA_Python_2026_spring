from selenium.webdriver.common.by import By

def test_start_page(browser):
    browser.get("https://scratch.mit.edu/")
    element = browser.find_element(By.ID, "navigation")

    assert "Create" in element.text