from selenium.webdriver.common.by import By

def test_build_history(browser):
    browser.find_element(By.CSS_SELECTOR, "a[href='/view/all/builds']").click()
    label = browser.find_element(By.CSS_SELECTOR, "div.jenkins-app-bar__content > h1").text

    assert label == "Build History of Jenkins"