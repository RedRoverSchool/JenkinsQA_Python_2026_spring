from selenium.webdriver.common.by import By

def test_language_menu(browser):
    browser.get("https://ebird.org/home")

    browser.find_element(By.ID, "language-menu-heading").click()
    elements = browser.find_elements(By.CSS_SELECTOR, "ul.u-textLanguageList li")

    assert len(elements) == 20
