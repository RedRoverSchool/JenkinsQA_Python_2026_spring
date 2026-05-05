import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_jenkins_ns(browser):
    browser.find_element(By.XPATH, "//*[@id='tasks']/div[1]/span/a").click()

    browser.find_element(By.ID, "name").send_keys("test_1")
    browser.find_element(By.XPATH,"//*[@id='j-add-item-type-standalone-projects']/ul/li[1]").click()
    browser.find_element(By.ID, "ok-button").click()
    #time.sleep(6)
    #browser.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()

    wait = WebDriverWait(browser, 11)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bottom-sticker']/div/button[1]"))).click()
    time.sleep(5)
    #label=browser.find_element(By.XPATH, "//*[@id='main-panel']/div[1]/div[1]/h1")
    wait = WebDriverWait(browser, 5)
    label=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='main-panel']/div[1]/div[1]/h1")))
    assert label.text == "test_1"