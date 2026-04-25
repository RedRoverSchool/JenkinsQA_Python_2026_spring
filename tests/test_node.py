import pytest
from selenium.webdriver.common.by import By

new_node_name = "New Test Node"
description = "Use only for urgent tasks"
dir = "D:\\Jenkins\\NewTestNode"
labels = "Urgent"

@pytest.fixture
def create_new_node(browser):
    browser.find_element(By.ID, "root-action-ManageJenkinsAction").click()
    browser.find_element(By.XPATH, "//a[@href='computer']").click()
    browser.find_element(By.XPATH, "//a[@href='new']").click()
    browser.find_element(By.ID, "name").send_keys(new_node_name)
    browser.find_element(By.CLASS_NAME, "jenkins-radio__label").click()
    browser.find_element(By.XPATH, "//button[@value='Create']").click()
    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    browser.find_element(By.XPATH, "//a[@href='../computer/%s/']" % new_node_name.replace(" ", "%20"))

def go_to_node_management_page(browser):
        browser.find_element(By.ID, "root-action-ManageJenkinsAction").click()
        browser.find_element(By.XPATH, "//a[@href='computer']").click()
        browser.find_element(By.XPATH, "//a[@href='../computer/%s/']" % new_node_name.replace(" ", "%20")).click()

def test_create_node(browser):

    browser.find_element(By.ID, "root-action-ManageJenkinsAction").click()
    browser.find_element(By.XPATH, "//a[@href='computer']").click()
    browser.find_element(By.XPATH, "//a[@href='new']").click()
    browser.find_element(By.ID, "name").send_keys(new_node_name)
    browser.find_element(By.CLASS_NAME, "jenkins-radio__label").click()
    browser.find_element(By.XPATH, "//button[@value='Create']").click()

    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    created_node = browser.find_element(By.XPATH, "//a[@href='../computer/%s/']" % new_node_name.replace(" ", "%20")).text

    assert new_node_name == created_node

def test_node_configuration(browser, create_new_node):

    expect_attributes= [description, labels]
    actual_attributes = []

    browser.find_element(By.ID, "root-action-ManageJenkinsAction").click()
    browser.find_element(By.XPATH, "//a[@href='computer']").click()
    browser.find_element(By.XPATH, "//a[@href='../computer/%s/']" % new_node_name.replace(" ", "%20")).click()
    browser.find_element(By.XPATH, "//a[@href='/computer/%s/configure']" % new_node_name.replace(" ", "%20")).click()
    browser.find_element(By.XPATH, "//textarea[@name='nodeDescription']").send_keys(description)
    browser.find_element(By.XPATH, "//input[@name='_.remoteFS']").send_keys(dir)
    browser.find_element(By.XPATH, "//input[@name='_.labelString']").send_keys(labels)
    browser.find_element(By.XPATH, "//select[@name='mode']").click()
    browser.find_element(By.XPATH, "//option[@value='EXCLUSIVE']").click()
    browser.find_element(By.XPATH, "//button[@value='Save']").click()

    actual_attributes.append(browser.find_element(By.ID, "description-content").text)
    actual_attributes.append(browser.find_element(By.XPATH, "//a[@href='/label/%s']" % labels).text)

    assert actual_attributes == expect_attributes

def test_mark_node_offline(browser, create_new_node):

    go_to_node_management_page(browser)

    browser.find_element(By.XPATH, "//form [@action='markOffline']").click()
    browser.find_element(By.XPATH, "//*[@id='main-panel']/form/p/button").click()

    expected_text = browser.find_element(By.CSS_SELECTOR, ".message")
    assert expected_text.text == "Disconnected by admin"