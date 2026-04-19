from selenium.webdriver.common.by import By


def test_text_web_tables(browser):

    browser.get("https://demoqa.com/webtables")
    browser.find_element(By.ID, "searchBox").send_keys("Alden")

    assert browser.find_element(By.CSS_SELECTOR, ".text-center").text == "Web Tables"
    rows = browser.find_elements(By.CSS_SELECTOR, ".table-bordered > tbody > tr")
    assert len(rows) == 1
    cells = browser.find_elements(By.CSS_SELECTOR, ".table-bordered > tbody > tr > td")
    assert "Alden" in cells[0].text