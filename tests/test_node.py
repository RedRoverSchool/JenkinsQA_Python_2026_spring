from selenium.webdriver.common.by import By

def test_create_node(browser):
    new_node_name = "New Test Node"

    browser.find_element(By.ID, "root-action-ManageJenkinsAction").click()
    browser.find_element(By.XPATH, "//a[@href='computer']").click()
    browser.find_element(By.XPATH, "//a[@href='new']").click()
    browser.find_element(By.ID, "name").send_keys(new_node_name)
    browser.find_element(By.CLASS_NAME, "jenkins-radio__label").click()
    browser.find_element(By.XPATH, "//button[@value='Create']").click()

    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    created_node = browser.find_element(By.XPATH, ("//a[@href='../computer/%s/']") % new_node_name.replace(" ", "%20")).text

    assert new_node_name == created_node
