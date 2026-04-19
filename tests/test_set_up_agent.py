
from selenium.webdriver.common.by import By

def test_create_agent(browser):
    browser.find_element(By.XPATH, '//a[@href="computer/new"]').click()
    browser.find_element(By.NAME, 'name').send_keys('agent name')
    browser.find_element(By.XPATH, "//input[@id='hudson.slaves.DumbSlave']/following-sibling::label").click()
    browser.find_element(By.NAME, 'Submit').click()

    browser.find_element(By.CSS_SELECTOR, '.setting-main [name="_.remoteFS"]').send_keys('/var/jenkins')
    browser.find_element(By.NAME, 'Submit').click()

    assert "/computer/" in browser.current_url