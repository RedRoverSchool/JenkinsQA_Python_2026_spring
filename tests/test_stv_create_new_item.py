import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # добавлено: явные ожидания вместо sleep
from selenium.webdriver.support import expected_conditions as EC  # добавлено: условия ожиданий


@pytest.mark.skip
def test_stv_create_new_item(browser):
    browser.find_element(By.XPATH, "//a[.//span[text()='New Item']]").click()


    assert "New Item" in browser.title

    browser.find_element(By.XPATH, "//input[@name='name']").send_keys("My_First_Test")

    browser.find_element(By.XPATH, '//div[@class="desc"]').click()

    browser.find_element(By.XPATH, '//button[@id="ok-button"]').click()
    WebDriverWait(browser, 10).until(  # заменено: ожидание загрузки страницы вместо time.sleep
        EC.visibility_of_element_located((By.XPATH, '//h2[@id="general"]'))
    )
    assert "General" in browser.find_element(By.XPATH, '//h2[@id="general"]').text
    browser.find_element(By.XPATH, '//*[@id="main-panel"]/form/div[1]/div[2]/div/div[2]/textarea').send_keys("My_First_Test")

    browser.find_element(By.XPATH, "//label[text()='Do not allow the pipeline to resume if the controller restarts']").click()

    element = browser.find_element(By.XPATH, "//label[normalize-space()='GitHub hook trigger for GITScm polling']")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

    element_save = browser.find_element(By.XPATH, "//button[@name = 'Submit']")
    browser.execute_script("arguments[0].scrollIntoView(true);", element_save)
    element_save.click()
    WebDriverWait(browser, 10).until(  # добавлено: ожидание обновления страницы после Save
        EC.title_contains("My_First_Test")
    )
    assert "My_First_Test" in browser.title

def test_stv_create_new_folder(browser):
    browser.find_element(By.XPATH, "//a[.//span[text()='New Item']]").click()
    browser.find_element(By.XPATH, "//input[@name='name']").send_keys("My_First_Folder")
    element_folder = browser.find_element(By.XPATH, '//span[@class="label" and text()="Folder"]')
    browser.execute_script("arguments[0].scrollIntoView(true);", element_folder)
    element_folder.click()
    element_ok = browser.find_element(By.XPATH, '//button[@id="ok-button"]')
    browser.execute_script("arguments[0].scrollIntoView(true);", element_ok)
    element_ok.click()
    WebDriverWait(browser, 10).until(  # заменено: ожидание загрузки конфигурации вместо sleep
        EC.visibility_of_element_located((By.XPATH, '//h2[@id="general"]'))
    )
    assert "General" in browser.find_element(By.XPATH, '//h2[@id="general"]').text
    browser.find_element(By.XPATH, '//input[@name="_.displayNameOrNull"]').send_keys("My_First_Folder")
    browser.find_element(By.XPATH, "//textarea[@name='_.description']").send_keys("My_First_Folder is created")
    browser.find_element(By.XPATH, '//button[@name = "Submit"]').click()

    WebDriverWait(browser, 10).until(  # добавлено: ожидание появления нового заголовка страницы
        EC.text_to_be_present_in_element((By.XPATH, '//h1'), "My_First_Folder")
    )
    assert "My_First_Folder" in browser.find_element(By.XPATH, '//h1').text