import time
from selenium.webdriver.common.by import By

def test_jenkins_create_job(browser):
    browser.find_element(By.LINK_TEXT, "Create a job").click()
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys("Free")
    browser.find_element(By.XPATH, "//span[@class='label' and text()='Freestyle project']").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//span[@class='jenkins-mobile-hide' and text()='Jenkins']").click()

    assert "Free" in browser.page_source
    time.sleep(3)



