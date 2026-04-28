from selenium.webdriver.common.by import By


def test_create_org_folder(browser):
    browser.find_element(By.XPATH, "//*[contains(concat(' ', @href, ' '), ' newJob ')]" ).click()
    browser.find_element(By.ID, "name").send_keys("Red Rover")
    browser.find_element(By.XPATH, "//*[@class='label'][.='Organization Folder']").click()
    browser.find_element(By.ID, "ok-button").click()
    browser.find_element(By.NAME, "_.displayNameOrNull").send_keys("JenkinsQA_Python_2026")
    browser.find_element(By.NAME, "_.description").send_keys("Very good Python automation course")
    browser.find_element(By.NAME, "Submit").click()

    display_name = browser.find_element(By.CSS_SELECTOR, "h1.job-index-headline").text.strip()
    description = browser.find_element(By.ID, "view-message").text.strip()

    assert display_name == "JenkinsQA_Python_2026"
    assert description == "Very good Python automation course"
