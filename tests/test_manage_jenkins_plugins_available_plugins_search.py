from selenium.webdriver.common.by import By
import pytest


@pytest.mark.skip()
def test_jenkins_plugins_available_plugins_search(browser):
    icon_setting = browser.find_element(By.XPATH, '//a[@id="root-action-ManageJenkinsAction"]')
    icon_setting.click()
    assert "/manage/" in browser.current_url

    plugins_element = browser.find_element(By.XPATH, '//a[@href= "pluginManager"]')
    plugins_element.click()
    assert "/pluginManager" in browser.current_url

    available_plugin_tab = browser.find_element(By.XPATH, "//a[@href='/manage/pluginManager/available']")
    available_plugin_tab.click()
    assert "available" in browser.current_url


    input_sort = browser.find_element(By.ID, "filter-box" )
    input_sort.send_keys("blue")
    assert  input_sort.get_attribute("value") == "blue"
    assert  "Blue Ocean" in browser.page_source



