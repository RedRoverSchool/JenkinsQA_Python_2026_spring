# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# def test_open_airtech():
#     driver = webdriver.Chrome()
#
# # Открытие страницы
#     print("Открытие тестовой страницы (https://www.airtechnology.ru/)...")
#     driver.get("https://www.airtechnology.ru/")
#     time.sleep(3)
#
# # Проверка заголовка
#     assert "Проектирование и монтаж инженерных систем | AIR TECHNOLOGY" in driver.title
#     print(f"Заголовок страницы: {driver.title}")
#     #
#     #     # Поиск элемента поиска по имени (name="q")
#     #     search_box = driver.find_element(By.XPATH, "//*[@id="ui-id-2"]/div[1]/img[1]")
#     #     search_box.click()
#     #
#     #    # Ждем 3 секунды, чтобы можно было визуально убедиться, что браузер открыт и текст введен
#     #     time.sleep(3)
#     #
#     # except Exception as e:
#     #     print(f"Произошла ошибка: {e}")
#     # finally:
#     #     print("Закрытие браузера...")
#     #     driver.quit()
#
#
# if __name__ == "__main__":
#     main()
#
