from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

button_url = "https://demoqa.com/buttons"

def test_button_double_click(browser):
    """
    Successful click on button 'Double Click Me'
    """

    browser.get(button_url)

    try:
        wait = WebDriverWait(browser, 10)
        button_double_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Double Click Me']")))

        ActionChains(browser).move_to_element(button_double_click).double_click(button_double_click).perform()

        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@id='doubleClickMessage']")))
        assert success_message.text == "You have done a double click"

    except TimeoutException:
        print("Кнопка не стала кликабельной за 10 секунд")
        raise

def test_button_right_click(browser):
    """
    Successful click on button 'Right Click Me'
    """

    browser.get(button_url)

    try:
        wait = WebDriverWait(browser, 10)
        button_right_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Right Click Me']")))
        ActionChains(browser).move_to_element(button_right_click).context_click(button_right_click).perform()

        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@id='rightClickMessage']")))

        assert success_message.text == "You have done a right click"

    except TimeoutException:
        print("Кнопка не стала кликабельной за 10 секунд")
        raise

def test_button_click(browser):
    """
    Successful click on button 'Click Me'
    """

    browser.get(button_url)

    try:
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))
        ActionChains(browser).move_to_element(button).click(button).perform()

        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@id='dynamicClickMessage']")))

        assert success_message.text == "You have done a dynamic click"

    except TimeoutException:
        print("Кнопка не стала кликабельной за 10 секунд")
        raise
