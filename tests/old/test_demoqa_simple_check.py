from selenium.webdriver.common.by import By


def test_widgets_text(browser):
    browser.get("https://demoqa.com/widgets")

    assert browser.find_element(
        By.XPATH,
        "//*[normalize-space()='Please select an item from left to start practice.']",
    ).text == "Please select an item from left to start practice."