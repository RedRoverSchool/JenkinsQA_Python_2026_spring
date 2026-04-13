from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login_enbek(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("https://passport.enbek.kz/kk/user/login")

    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("test@test.com")
    browser.find_element(By.ID, "password").send_keys("wrongpassword")
    browser.find_element(By.CSS_SELECTOR, "button[wire\\:target='login']").click()

    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-red-500")))
    assert error.is_displayed()