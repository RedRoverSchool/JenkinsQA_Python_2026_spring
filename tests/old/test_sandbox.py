from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://aqa-proka4.org/sandbox/web"

def test_validation_form(browser):
    password = "password1"

    browser.get(url + "#forms")
    browser.find_element(By.ID, "val-username").send_keys("Emilia")
    browser.find_element(By.ID, "val-email").send_keys("emilia@mail.ru")
    browser.find_element(By.ID, "val-password").send_keys(password)
    browser.find_element(By.ID, "val-confirm-password").send_keys(password)
    browser.find_element(By.ID, "valSubmitBtn").click()
    success_element = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='valFormResult']/div/p"))
    )
    assert "Все проверки пройдены! Форма валидна." in success_element.text, \
        f"Ожидалось сообщение об успехе, получили: '{success_element.text}'"

def test_appearing_elements(browser):
    expected_names = ["Элемент 1", "Элемент 2", "Элемент 3"]

    browser.get(url + "#dynamic")
    browser.find_element(By.ID,"showDelayedBtn").click()

    wait = WebDriverWait(browser, 3)
    elements = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='delayedContent']//h4"))
    )
    actual_names = [element.text for element in elements]

    assert len(elements) == 3, f"Найдено {len(actual_names)} элементов, должно быть 3"
    assert actual_names == expected_names, \
        f"Ожидалось: {expected_names}, получено: {actual_names}"