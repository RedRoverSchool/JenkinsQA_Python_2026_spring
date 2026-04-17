from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

demoqa_url = "https://demoqa.com/"

def test_check_open_alert(browser):
    browser.get(demoqa_url)

    browser.find_element(By.XPATH, "//a[@href='/alertsWindows']").click()
    browser.find_element(By.XPATH, "//span[text()='Alerts']").click()
    browser.find_element(By.ID, "confirmButton").click()

    alert = browser.switch_to.alert
    alert.accept()

    assert browser.find_element(By.ID, "confirmResult").text == "You selected Ok"

def test_check_switch_new_tab(browser):
    browser.get(demoqa_url)

    browser.find_element(By.XPATH, "//a[@href='/alertsWindows']").click()
    browser.find_element(By.XPATH, "//span[text()='Browser Windows']").click()
    browser.find_element(By.ID, "tabButton").click()

    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[1])

    assert browser.find_element(By.ID, "sampleHeading").text == "This is a sample page"

def test_check_field_tooltip(browser):
    browser.get("https://play-qa.ru/")

    browser.find_element(By.XPATH, "//a[@href='/interactive']").click()

    browser.find_element(By.ID, "popover-button").click()

    tooltip_block = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='popover-content']"))).text

    assert "Содержимое всплывающего окна" in tooltip_block

