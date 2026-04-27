from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_dropdown(browser):
    avatar = browser.find_element(By.XPATH, "//a[@id='root-action-UserAction']")
    actions = ActionChains(browser)
    '''Ведем мышь до элемента, который открывает дропдаун'''
    actions.move_to_element(avatar).perform()
    dropdown_menu = browser.find_element(By.XPATH, "//div[@class='tippy-box']")
    '''Проверка, что всплывающее меню отображается'''
    assert dropdown_menu.is_displayed()

