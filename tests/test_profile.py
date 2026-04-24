import time
from selenium.webdriver.common.by import By

def test_profile(browser):
    profile = browser.find_element(By.CLASS_NAME, "jenkins-avatar")
    profile.click()
    option = browser.find_element(By.XPATH, '// *[ @ id = "tasks"] / div[1] / span / a / span[2]')
    assert option.text == "Profile"
    # element = browser.find_element(By.XPATH, '//*[@id="breadcrumbs"]/li/span')
    # assert element.text == "Tatyana"