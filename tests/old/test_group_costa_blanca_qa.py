from selenium.webdriver.common.by import By
import time


def test_storyia_submit_form(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = browser.find_element(By.NAME, "my-text")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button")

    text_box.send_keys("Storyia")
    submit_button.click()

    message = browser.find_element(By.ID, "message").text

    assert message == "Received!"

def test_storyia_checkbox_selected(browser):
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    checkbox = browser.find_element(By.ID, "my-check-2")
    checkbox.click()

    assert checkbox.is_selected()





def test_title_sergio_qa(browser):
    '''Тест проверки заголовка страницы'''
    browser.get('https://martspec.com/')
    assert 'Simplify health & wellness tracking' in browser.title

def test_change_language_sergio_qa(browser):
    '''Раскрыть список языков веб-сайта'''
    browser.get('https://martspec.com/')

    dropdown = browser.find_element(By.ID, 'navbarDropdown')
    dropdown.click()

    time.sleep(3)


def test_elena_color_picker_value(browser):
    """Тест на изменение значения в палитре цветов"""
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    color_input = browser.find_element(By.NAME, "my-colors")
    target_color = "#ff0000"
    color_input.send_keys(target_color)

    assert color_input.get_attribute("value") == target_color
