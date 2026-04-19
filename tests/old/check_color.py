from selenium import webdriver
from selenium.webdriver.common.by import By

def test_color_picker():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        driver.implicitly_wait(0.5)

        color_picker = driver.find_element(by=By.NAME, value="my-colors")

        current_color = color_picker.get_attribute("value")
        print(f"Текущий цвет: {current_color}")

        assert current_color == "#563d7c", f"Ожидался #563d7c, получен {current_color}"

        print("✓ Цвет установлен корректно!")

    finally:
        driver.quit()