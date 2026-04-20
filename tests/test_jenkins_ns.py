import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip
def test_jenkins_ns(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.ID, "name").send_keys("test_1")
    browser.find_element(By.XPATH,"//*[@id='j-add-item-type-standalone-projects']/ul/li[1]").click()
    browser.find_element(By.ID, "ok-button").click()
    # time.sleep(3)
    button1=WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='bottom-sticker']/div/button[1]"))
    )
    # browser.find_element(By.XPATH, "//*[@id='bottom-sticker']/div/button[1]").click()
    button1.click()

    label=browser.find_element(By.XPATH, "//*[@id='main-panel']/div[1]/div[1]/h1")

    assert label.text == "test_1"