import time
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize("valid_name", [
    # Только буквы
    "myitem",
    "MyItem",
    "ITEM",

    # Только цифры
    "123",
    "0",

    # Буквы + цифры
    "myitem123",
    "123myitem",
    "myitem123myitem",

    # Дефис (в разных позициях)
    "my-item",
    "-item",
    "item-",
    "my--item",  # два дефиса подряд
    "-my-item-",

    # Подчеркивание (в разных позициях)
    "my_item",
    "_item",
    "item_",
    "my__item",  # два подчеркивания подряд
    "_my_item_",

    # Комбинации
    "my-item_123",
    "my_item-123",
    "My_Item-2024_test",
    "-my_item-123_",

    # Граничные значения
    "a",  # 1 символ
    "a" * 255,  # 255 символов (максимум)
    "a-b-c-1-2-3",  # много дефисов
    "a_b_c_1_2_3",  # много подчеркиваний
])

    
def test_valid_input_item_name(browser, valid_name):
    new_item_button = browser.find_element(By.XPATH, "//a[contains(., 'New Item')]")
    new_item_button.click()

# находим поле ввода
    input_item_name = browser.find_element(By.ID, "name")
    assert input_item_name.is_displayed(), "Input 'Enter an item name' not found"

    input_item_name.clear()
    input_item_name.send_keys(valid_name)
    browser.find_element(By.TAG_NAME, "body").click()
    time.sleep(0.5)

    errors = browser.find_elements(By.CLASS_NAME, "input-validation-message")

    visible_errors = [
        e.text for e in errors
        if e.is_displayed() and e.text.strip() != ""
    ]

    assert len(visible_errors) == 0, f"Найдены ошибки: {visible_errors}"


@pytest.mark.parametrize("invalid_name", [
    # Пробелы - Jenkins разрешает

    # Русские буквы - Jenkins разрешает

    # Спецсимволы
    "my@item",  # @
    "my#item",  # #
    "my$item",  # $
    "my%item",  # %
    "my^item",  # ^
    "my&item",  # &
    "my*item",  # *
    # "my(item)",  # Jenkins разрешает ( )
    # "my+item",  # Jenkins разрешает +
    # "my=item",  # Jenkins разрешает =
    # "my~item",  # Jenkins разрешает ~
    "my:item",  # :
    "my;item",  # ;
    "my<item>",  # < >
    # "my,item",  # Jenkins разрешает ,
    # "my.item",  # Jenkins разрешает .
    "my?item",  # ?
    "my/item",  # /
    "my\\item",  # \
    "my|item",  # |
    "my[item]",  # [ ]
    # "my{item}",  # Jenkins разрешает {}
    # "my`item",  # Jenkins разрешает `
    # "my'item",  # Jenkins разрешает '
    # 'my"item',  # Jenkins разрешает "
    "my!item",  # !

    # Пустые
    "",

    # Только спецсимволы
    # "---",
    # "___",
    "!@#$%",
])

def test_invalid_input_item_name(browser, invalid_name):
    new_item_button = browser.find_element(By.XPATH, "//a[contains(., 'New Item')]")
    new_item_button.click()
    time.sleep(0.5)

# находим поле ввода
    input_item_name = browser.find_element(By.ID, "name")
    assert input_item_name.is_displayed(), "Input 'Enter an item name' not found"

    input_item_name.clear()
    input_item_name.send_keys(invalid_name)
    browser.find_element(By.TAG_NAME, "body").click()
    time.sleep(0.5)

    errors = browser.find_elements(By.CLASS_NAME, "input-validation-message")

    visible_errors = [
        e.text for e in errors
        if e.is_displayed() and e.text.strip() != ""
    ]

    assert len(visible_errors) > 0, \
        f"Ошибка не появилась для значения '{invalid_name}'"




