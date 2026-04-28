import time
from selenium.webdriver.common.by import By

def test_create(browser):
    browser.find_element(By.CLASS_NAME, "content-block__link").click()
    browser.find_element(By.ID, "name").send_keys("Test")
    browser.find_element(By.XPATH, "//span[@class='label' and text()='Freestyle project']").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.CSS_SELECTOR, "button.jenkins-submit-button").click()

    time.sleep(5)

    browser.find_element(By.XPATH, "//span[normalize-space()='Jenkins']").click()

    rows = browser.find_elements(By.CSS_SELECTOR, "table#projectstatus tbody tr")

    assert len(rows) == 1
    assert "Test" in rows[0].text