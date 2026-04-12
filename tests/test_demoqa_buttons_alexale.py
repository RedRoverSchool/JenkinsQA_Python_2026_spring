from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


button_url = 'https://demoqa.com/buttons'


def test_button_double_click(browser):
    """
    Successful click on button 'Double Click Me'
    """

    browser.get(button_url)
    action = ActionChains(browser)
    double_click_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "doubleClickBtn"))
    )

    time.sleep(1)
    action.double_click(double_click_button).perform()

    appeared_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'doubleClickMessage'))
    )

    assert appeared_element.text == 'You have done a double click'


def test_button_right_click(browser):
    """
    Successful click on button 'Right Click Me'
    """

    browser.get(button_url)
    action = ActionChains(browser)
    right_click_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'rightClickBtn'))
    )

    time.sleep(1)
    action.context_click(right_click_button).perform()

    appeared_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'rightClickMessage'))
    )

    assert appeared_element.text == 'You have done a right click'


def test_button_click(browser):
    """
    Successful click on button 'Click Me'
    """

    browser.get(button_url)
    click_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[text()="Click Me"]'))
    )

    time.sleep(1)
    click_button.click()

    appeared_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'dynamicClickMessage'))
    )

    assert appeared_element.text == 'You have done a dynamic click'
