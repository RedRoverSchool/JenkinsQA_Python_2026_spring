from selenium.webdriver.common.by import By

def test_wikipedia_python_search(browser):
    browser.implicitly_wait(10)
    browser.get("https://ru.wikipedia.org/")

    search_input = browser.find_element(By.ID, "searchInput")
    search_input.send_keys("Python")
    search_button = browser.find_element(By.CSS_SELECTOR, "button.cdx-search-input__end-button")
    search_button.click()
    page_header = browser.find_element(By.ID, "firstHeading")

    assert "Python" in page_header.text, f"Ожидали Python, а получили: {page_header.text}"