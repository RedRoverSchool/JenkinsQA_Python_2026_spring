from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

invalid_chars = ["?", "*", "/", ".", "!", "%", "$", '&',  ";", ":)", "|"]

input_field = (By.ID, "name")
select_new_item_button = (By.XPATH, "//a[@it]")
error_locator = (By.XPATH, '//*[@id="itemname-invalid"]')
freestyle_project_type = (By.CLASS_NAME, "hudson_model_FreeStyleProject")

def test_invalid_characters(browser):

    browser.find_element(*select_new_item_button).click()
    wait = WebDriverWait(browser, 10)

    browser.find_element(*freestyle_project_type).click()

    for char in invalid_chars:
        browser.find_element(*input_field)
        browser.find_element(*input_field).clear()
        browser.find_element(*input_field).send_keys(char)

        error_message = wait.until(EC.visibility_of_element_located(error_locator))
        assert "небезопасный символ" or "is not an allowed name" in error_message.text
        ok_button = browser.find_element(By.ID, "ok-button")
        assert not ok_button.is_enabled(), "Кнопка ОК должна быть неактивна при наличии спецсимволов"