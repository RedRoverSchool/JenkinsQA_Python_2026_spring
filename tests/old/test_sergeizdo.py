from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

Selenium_page = "https://www.selenium.dev/selenium/web/web-form.html"
Wiki_page = "https://en.wikipedia.org/wiki/Main_Page"

def test_selenium_page(browser):

    browser.get(Selenium_page)
    browser.implicitly_wait(0.5)

    text_box = browser.find_element(by=By.NAME, value="my-textarea")
    text_box.send_keys("My city")

#         Dropdowns
    dropdown_select = browser.find_element(By.NAME, "my-select")
    select = Select(dropdown_select)

    select.select_by_visible_text("Two")

    assert select.first_selected_option.text == "Two"

    dropdown_datalist = browser.find_element(by=By.NAME, value="my-datalist")
    dropdown_datalist.send_keys("San Francisco")

#       Checkboxes etc
    checked_checkbox = browser.find_element(By.ID, "my-check-1")
    checked_checkbox.click()

    Checked_radio = browser.find_element(By.ID, "my-radio-1")
    Checked_radio.click()

    assert Checked_radio.is_selected()

    submit_button = browser.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()


#               Test WIKIPEDIA
def test_wiki_search_box(browser):

    browser.get(Wiki_page)
    browser.get("https://en.wikipedia.org/wiki/Main_Page")

    browser.implicitly_wait(0.5)

    search_box = browser.find_element(By.ID, "searchInput")

    search_box.send_keys("Selenium")

    search_button = browser.find_element(By.CSS_SELECTOR, "button.cdx-search-input__end-button")
    search_button.click()