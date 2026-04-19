from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_simple_drag_and_drop(browser):
    browser.get("https://demoqa.com/droppable")

    simple_tab = browser.find_element(By.ID, "droppableExample-tab-simple")
    simple_tab.click()

    drag_element = browser.find_element(By.ID, "draggable")
    drop_element = browser.find_element(By.ID, "droppable")

    ActionChains(browser).drag_and_drop(drag_element, drop_element).perform()

    assert drop_element.text == "Dropped!"
