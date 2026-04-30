from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

def test_add_credentials_ssh_username(browser):
    browser.find_element(By.ID, 'root-action-ManageJenkinsAction').click()
    browser.find_element(By.XPATH, "//*[@href='credentials']").click()
    browser.find_element(By.XPATH, "(//button[@class='jenkins-menu-dropdown-chevron'])[2]").click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Add credentials'])[1]"))).click()

    test_id = "testID"
    description = "testDescription"
    kind = "SSH Username with private key"

    select_scope = Select(browser.find_element(By.XPATH,"(//select[@name='_.scope'])[1]"))
    select_scope.select_by_value('SYSTEM')

    select_kind = Select(browser.find_element(By.CSS_SELECTOR, ".jenkins-select__input"))
    select_kind.select_by_value('2')

    browser.find_element(By.XPATH, "//*[@checkurl='/manage/descriptorByName/com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey/checkId']").send_keys(test_id)
    browser.find_element(By.XPATH, "(//input[@name='_.description'])[2]").send_keys(description)
    browser.find_element(By.XPATH, "(//input[@name='_.username'])[2]").send_keys("testUsername")
    browser.find_element(By.XPATH, "(//label[contains(@class,'attach-previous') and contains(text(),'Treat username as secret')])[2]").click()
    browser.find_element(By.XPATH, "//label[normalize-space()='Enter directly']").click()
    browser.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    browser.find_element(By.XPATH, "//textarea").send_keys("testKey")
    browser.find_element(By.XPATH, "// input[ @ name = '_.passphrase']").send_keys("testPassphrase")
    browser.find_element(By.XPATH, "//button[normalize-space()='Create']").click()

    assert (
            browser.find_element(By.XPATH, "//a[normalize-space()='testID']").text == test_id and
            browser.find_element(By.XPATH, "(//td[contains(text(), 'testDescription')])[1]").text == description and
            browser.find_element(By.XPATH, "(//td[contains(text(), 'SSH Username with private key')])").text == kind and
            browser.find_element(By.XPATH, "(//td[contains(text(), 'testDescription')])[2]").text == description
    )





