from selenium.webdriver.common.by import By


def test_click_download_button(browser):
    browser.get("https://www.python.org")

    download_button = browser.find_element(By.LINK_TEXT, "Downloads")
    download_button.click()

    assert "downloads" in browser.current_url.lower()
    print("Успешно!")