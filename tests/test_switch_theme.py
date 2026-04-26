from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_user_can_switch_theme(browser):
    user_icon = (By.XPATH, "//a[@id='root-action-UserAction']")
    theme_label = (By.XPATH, "//select[@id='account-theme-picker']")
    dark_opt = (By.XPATH, "//*[text()='Dark']")
    theme_span = (By.XPATH, "//label[@class='jenkins-dropdown__item tm-account-theme-picker-select']/span")

    ActionChains(browser).move_to_element(browser.find_element(*user_icon)).perform()  # курсор в меню
    browser.find_element(*theme_label).click()  # тык поле тема
    browser.find_element(*dark_opt).click()  # тык темная

    theme_text = browser.find_element(*theme_span).text  # получаем текст в поле тема
    assert theme_text == "Dark", "Ooop"
