from selenium import webdriver
from selenium.webdriver.common.by import By

def test_placeholder():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        disabled_input = driver.find_element(By.CSS_SELECTOR, "input[disabled]")
        placeholder_text = disabled_input.get_attribute("placeholder")
        assert placeholder_text == "Disabled input", f"Текс лейсхолдера несоответсвует ОР. ФР:{disabled_input}"

    finally:
        driver.quit()

