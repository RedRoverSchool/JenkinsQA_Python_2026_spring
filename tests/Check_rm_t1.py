import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

input_name_locator = (By.XPATH, '//input[@name="query"]')
# input_news_locator = (By.XPATH, '//div[@search-type="news"]')
# cookie_accept_locator = (
#     By.XPATH,
#     '//button[contains(text(), "Принять все cookie")]',
# )  # может отличаться текст


def main():
    print("Инициализация браузера Chrome...")

    # Настройка опций (опционально)
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Раскомментируйте для скрытого режима, если не хотите видеть окно браузера

    # Инициализация веб-драйвера с помощью webdriver-manager (автоматически скачает нужный chromedriver)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Открытие страницы
        print("Открытие тестовой страницы (onliner.by)...")
        driver.get("https://www.onliner.by/")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(input_name_locator)
        )

        driver.find_element(*input_name_locator).send_keys("Стол")
        time.sleep(5)
        # try:
        #     cookie_accept = WebDriverWait(driver, 5).until(
        #         EC.element_to_be_clickable(cookie_accept_locator)
        #     )
        #     cookie_accept.click()
        #     print("Cookies приняты")
        # except Exception as e:
        #     print("Окно cookies не появилось или уже обработано:", e)
        # time.sleep(5)

        # driver.find_element(*input_news_locator).click()

        print("Ready!:)")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Закрытие браузера...")
        driver.quit()


if __name__ == "__main__":
    main()
