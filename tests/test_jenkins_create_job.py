import time
from selenium.webdriver.common.by import By


# @pytest.mark.skip()
def test_jenkins_create_job(browser):
    browser.find_element(By.LINK_TEXT, "Create a job").click()

    time.sleep(5)

    assert "New Item" in browser.page_source

    browser.find_element(By.XPATH, "//input[@id='name']").send_keys("Pipeline")
    browser.find_element(By.XPATH, "//span[@class='label' and text()='Pipeline']").click()

    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()

    time.sleep(5)
    assert "General" in browser.page_source
