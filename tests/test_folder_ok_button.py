import pytest
from selenium.webdriver.common.by import By
# TC_01.002.03 | New Item > Folder > Verify buttom OK is able after selecting the Folder type and entering an item name
# ID: TC_01.002.03 | Новый элемент > Папка > Убедитесь, что кнопка «ОК» активна после выбора типа папки и
# ввода имени элемента.
# Предварительные условия:
# Открыта страница «Новый элемент».
#
# Описание:
# Кнопку «ОК» можно нажать после выбора типа папки и ввода имени элемента.
#
# Шаги:
# Введите название товара
# Нажмите на папку
# Ожидаемый результат:
# Кнопка OK доступна
@pytest.mark.skip()
def test_ok_button_enabled_for_folder(browser):
    browser.get("http://localhost:8080/view/all/newJob")
    element = browser.find_element (By.XPATH, "//input[@name='name']")
    element.send_keys("TestFolder")
    folder = browser.find_element(By.XPATH, "//li[contains(@class,'folder_Folder')]")
    folder.click()
    ok_button = browser.find_element(By.ID, "ok-button")
    assert ok_button.is_displayed()
