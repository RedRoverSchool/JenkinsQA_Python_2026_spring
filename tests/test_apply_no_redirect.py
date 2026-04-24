from selenium.webdriver.common.by import By

def test_apply_no_redirect(browser):
    """
    Проверка отсутствия редиректа при сохранении изменений с помощью кнопки Apply
    """
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.XPATH, "//input[@name='name']").click()
    browser.find_element(By.XPATH, "//input[@name='name']").send_keys("Test_Freestyle_Project")
    browser.find_element(By.XPATH, "//li[@class='hudson_model_FreeStyleProject']").click()

    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()

    description = browser.find_element(By.XPATH, "//textarea[@name='description']")
    description.click()
    description.send_keys("Description test")

    browser.find_element(By.XPATH, "//button[@name='Apply']").click()
    assert "/job/Test_Freestyle_Project/configure" in browser.current_url, f"Выполнен редирект со страницы конфигурации "
