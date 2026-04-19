from selenium import webdriver
from selenium.webdriver.common.by import By

def test_fill_practice_hub():
    driver = webdriver.Chrome()

    driver.get("https://lms.threadqa.ru/xpath-practice-hub")
    driver.implicitly_wait(0.5)

    driver.find_element(By.CSS_SELECTOR, "[data-testid='username-field']").send_keys("Alexander")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='email-field']").send_keys("test@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='password-field']").send_keys("12345678")
    driver.find_element(By.CSS_SELECTOR, "[data-testid='comment-field']").send_keys(
        "Это очень плохой тест, очень сложно и не понятно, что мы тут вообще делаем....."
    )

    assert driver.find_element(By.CSS_SELECTOR, "[data-testid='username-field']").get_attribute("value") == "Alexander"
    assert driver.find_element(By.CSS_SELECTOR, "[data-testid='email-field']").get_attribute("value") == "test@gmail.com"
    assert driver.find_element(By.CSS_SELECTOR, "[data-testid='password-field']").get_attribute("value") == "12345678"
    assert "Это очень плохой тест" in driver.find_element(By.CSS_SELECTOR, "[data-testid='comment-field']").get_attribute("value")

    driver.quit()

