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

@pytest.fixture
def go_to_node_management_page(browser, create_new_node):
    browser.find_element(By.ID, "root-action-ManageJenkinsAction").click()
    browser.find_element(By.XPATH, "//a[@href='computer']").click()
    browser.find_element(By.XPATH, "//a[@href='../computer/%s/']" % new_node_name.replace(" ", "%20")).click()

@pytest.fixture
def mark_node_offline(browser, go_to_node_management_page):

    browser.find_element(By.XPATH, "//form [@action='markOffline']").click()
    browser.find_element(By.XPATH, "//*[@id='main-panel']/form/p/button").click()

@pytest.fixture
def bring_node_online(browser, mark_node_offline):
    browser.find_element(By.XPATH, "//button [@value ='Bring this node back online']").click()
    browser.find_element(By.XPATH, "//form [@action='markOffline']")

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

def test_node_configuration(browser, go_to_node_management_page):

    expect_attributes= [description, labels]
    actual_attributes = []

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

def test_mark_node_offline(browser, go_to_node_management_page):

    browser.find_element(By.XPATH, "//form [@action='markOffline']").click()
    browser.find_element(By.XPATH, "//*[@id='main-panel']/form/p/button").click()

    expected_text = browser.find_element(By.CSS_SELECTOR, ".message")
    assert expected_text.text == "Disconnected by admin"

def test_bring_node_online(browser, mark_node_offline):

    browser.find_element(By.XPATH, "//button [@value ='Bring this node back online']").click()

    assert browser.find_element(By.XPATH, "//form [@action='markOffline']").text == "Mark this node temporarily offline"

def test_delete_node(browser, bring_node_online):

    browser.find_element(By.CLASS_NAME, "icon-edit-delete").click()
    browser.find_element(By.XPATH, "//button [@data-id='ok']").click()

    actual_node_list = browser.find_elements(By.XPATH, "//a[@class = 'jenkins-table__link model-link inside']")

    node_names = [node.text for node in actual_node_list]

    assert new_node_name not in node_names

