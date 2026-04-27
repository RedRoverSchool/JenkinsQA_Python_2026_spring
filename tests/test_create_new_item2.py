from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_apply_new_item(browser):
    name_freestyle_project = "Test_Freestyle_Project"

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.XPATH, "//input[@name='name']").send_keys(name_freestyle_project)
    browser.find_element(By.XPATH, "//li[@class='hudson_model_FreeStyleProject']").click()
    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
    browser.find_element(By.XPATH, "//button[@name='Apply']").click()

    """Проверяется отсутствие редиректа после нажатия на кнопку Apply """
    current_page_name = browser.find_element(By.XPATH,"//a[@href = '/job/Test_Freestyle_Project/']").text
    assert current_page_name == name_freestyle_project , f"Выполнен редирект со страницы конфигурации "

    """Проверяется появление уведомления с текстом 'Saved' после нажатия на кнопку Apply.
       Используется wait, т.к элемент существует в DOM, но ещё не виден."""
    message_apply = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='notification-bar']/span"))
    ).text
    assert message_apply == "Saved", f"Текст не совпадает, отображается текст {message_apply}"
