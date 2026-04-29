import time
from selenium.webdriver.common.by import By

def test_jenkins_ns(browser):
    browser.find_element(By.LINK_TEXT, "New Item").click()

    browser.find_element(By.ID, "name").send_keys("test_1")
    browser.find_element(By.XPATH,"//ul/li//span[text()='Pipeline']").click()
    browser.find_element(By.ID, "ok-button").click()
    time.sleep(6)

    browser.find_element(By.NAME,"Submit").click()
    time.sleep(5)

    browser.find_element(By.XPATH, "//*[@class='app-jenkins-logo']").click()
    time.sleep(2)

    label=browser.find_element(By.XPATH, "//*[@href='job/test_1/']")
    assert label.text == "test_1"
