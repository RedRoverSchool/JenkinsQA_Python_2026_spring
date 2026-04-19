from selenium.webdriver.common.by import By

URL = "https://demoqa.com/checkbox"

switcher_home = (By.XPATH, "//span[@class='rc-tree-switcher rc-tree-switcher_close']")
switcher_desktop = (By.XPATH, "//span[@class='rc-tree-switcher rc-tree-switcher_close']")
checkbox_notes = (By.XPATH, "(//span[@class='rc-tree-checkbox'])[3]")
result = (By.XPATH, "//div[@id='result']")


def test_selected_notes_checkbox(browser):
    browser.get(URL)
    browser.find_element(*switcher_home).click()
    browser.find_element(*switcher_desktop).click()
    browser.find_element(*checkbox_notes).click()

    result_text = browser.find_element(*result).text
    assert result_text.split()[-1] == 'notes', "такс, а где 'notes'?"
