from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcon

items = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder",
         "Multibranch Pipeline", "Organization Folder"]

def test_new_items(browser):
    for item_name in items:
        browser.find_element(By.XPATH, '//*[@href="/view/all/newJob"]').click()
        browser.find_element(By.XPATH, "//*[@id='name']").send_keys(f"{item_name}_1")
        browser.find_element(By.XPATH, f"//span[text()='{item_name}']").click()
        browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
        wait = WebDriverWait(browser, 10)
        wait.until(expcon.element_to_be_clickable((By.ID, "jenkins-head-icon"))).click()

        item_url = item_name.replace(" ", "%20")
        actions = ActionChains(browser)
        parent_element = browser.find_element(By.XPATH, f"//*[@href='job/{item_url}_1/']")
        actions.move_to_element(parent_element).perform()
        browser.find_element(By.XPATH, f"//button[contains(@data-href, '/job/{item_url}_1/')]").click()
        browser.find_element(By.XPATH, "//button[contains(@href, 'doDelete')]").click()
        browser.find_element(By.XPATH, "//button[@data-id='ok']").click()
        wait = WebDriverWait(browser, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "jenkins-head-icon"))).click()
        assert f"{item_name}_1" not in browser.page_source
