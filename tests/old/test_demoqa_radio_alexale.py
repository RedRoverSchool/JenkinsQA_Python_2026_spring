from selenium.webdriver.common.by import By


radio_button_url = 'https://demoqa.com/radio-button'


def test_radio_button_yes(browser):
    """
    Successful click on radio-button 'Yes'
    """

    browser.get(radio_button_url)
    yes_radio_button = browser.find_element(By.ID, 'yesRadio')
    yes_radio_button.click()

    appeared_element = browser.find_element(By.XPATH, '//*[contains(@class, "mt-3")]')

    assert appeared_element.text == 'You have selected Yes'


def test_radio_button_impressive(browser):
    """
    Successful click on radio-button 'Impressive'
    """

    browser.get(radio_button_url)
    impressive_radio_button = browser.find_element(By.ID, 'impressiveRadio')
    impressive_radio_button.click()

    appeared_element = browser.find_element(By.XPATH, '//*[contains(@class, "mt-3")]')

    assert appeared_element.text == 'You have selected Impressive'


def test_radio_button_no(browser):
    """
    Radio-button 'No' is disabled
    """

    browser.get(radio_button_url)
    no_radio_button = browser.find_element(By.ID, 'noRadio')

    assert not no_radio_button.is_enabled()
