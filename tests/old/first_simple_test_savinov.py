import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    print("Инициализация браузера Chrome...")

    options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Открытие сайта...")
        driver.get("https://demoqa.com/")

        print(driver.title)

        # 🔹 Клик по Elements (CSS)
        elements_card = driver.find_element(By.CSS_SELECTOR, "div.card-body h5")
        elements_card.click()

        actions = ActionChains(driver)

        #  Клик по вкладке Buttons (CSS)
        btn_menu = driver.find_element(By.CSS_SELECTOR, "#item-4 span")
        btn_menu.click()

        #  Клик по Double Click Me (ID)
        btn_double_click = driver.find_element(By.ID, "doubleClickBtn")
        actions.double_click(btn_double_click).perform()
        assert driver.find_element(By.ID, "doubleClickMessage").text == "You have done a double click"


        # Клик по Right Click Me (ID)
        btn_right_click = driver.find_element(By.ID, "rightClickBtn")
        actions.context_click(btn_right_click).perform()
        assert driver.find_element(By.ID, "rightClickMessage").text == "You have done a right click"

        # Клик по  Click Me (XPATH)
        btn_click_me = driver.find_element(By.XPATH, "//button[text()='Click Me']")
        btn_click_me.click()
        assert driver.find_element(By.ID, "dynamicClickMessage").text == "You have done a dynamic click"
        print("Тест выполнен успешно!")




    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        print("Закрытие браузера...")
        driver.quit()


if __name__ == "__main__":
    main()