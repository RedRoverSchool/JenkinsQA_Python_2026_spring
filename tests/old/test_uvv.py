import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


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
        print("Открытие тестовой страницы (python.org)...")
        driver.get("https://www.python.org/")

        # Проверка заголовка
        assert "Python" in driver.title
        print(f"Заголовок страницы: {driver.title}")

        # Поиск элемента поиска по имени (name="q")
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()

        # Ввод текста
        print("Вводим текст 'selenium' в строку поиска...")
        search_box.send_keys("selenium")

        # Ждем 3 секунды, чтобы можно было визуально убедиться, что браузер открыт и текст введен
        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Закрытие браузера...")
        driver.quit()


if __name__ == "__main__":
    main()




