from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



@pytest.mark.skip
def test_apply_shows_message(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()

    browser.find_element(By.XPATH, "//input[@name='name']").click()
    browser.find_element(By.XPATH, "//input[@name='name']").send_keys("Test_Freestyle_Project")

    browser.find_element(By.XPATH, "//li[@class='hudson_model_FreeStyleProject']").click()

    browser.find_element(By.XPATH, "//button[@id='ok-button']").click()

    browser.find_element(By.XPATH, "//textarea[@name='description']").click()
    browser.find_element(By.XPATH, "//textarea[@name='description']").send_keys("Description test")

    browser.find_element(By.XPATH, "//button[@name='Apply']").click()

    message_apply = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@id='notification-bar']")))
    assert "Saved" in message_apply.text, f"Текст не совпадает, отображается текст {message_apply.text}"


