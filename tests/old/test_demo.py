from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

input_name_locator = (By.XPATH, "//input[@id='firstName']")
input_last_name_locator = (By.XPATH, "//input[@id='lastName']")
input_email_locator = (By.XPATH, "//input[@id='email']")
input_phone_locator = (By.XPATH, "//input[@id='phone']")
input_dateOfBirth_locator = (By.XPATH, "//input[@id='dob']")
input_gender_male_locator = (By.XPATH, "//input[@id='gender-male']")
input_city_locator = (By.XPATH, "//input[@id='city']")
input_password_locator = (By.XPATH, "//input[@id='password']")
input_confirm_password_locator = (By.XPATH, "//input[@id='confirmPassword']")
button_terms_locator = (By.XPATH, "//button[@id='terms']")
button_submit_locator = (By.XPATH, "//button[@id='submitFormBtn']")
button_fill_again_locator = (By.XPATH, "//button[@id='resetFormBtn']")


def demo():
    print("Инициализация браузера Chrome...")

    options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Открытие тестовой страницы (https://www.qaplayground.com/practice/forms)...")
        driver.get("https://www.qaplayground.com/practice/forms")
        driver.find_element(*input_name_locator).send_keys("Elena")
        driver.find_element(*input_last_name_locator).send_keys("Nov")
        driver.find_element(*input_email_locator).send_keys("email@mail.com")
        driver.find_element(*input_phone_locator).send_keys("7777777777")
        driver.find_element(*input_dateOfBirth_locator).send_keys("01/01/2000")
        driver.find_element(*input_gender_male_locator).click()

        driver.execute_script("""
            const select = document.querySelector('select[aria-hidden="true"]');
            select.value = 'india';
            select.dispatchEvent(new Event('change', { bubbles: true }));
        """)
        driver.find_element(*input_city_locator).send_keys("Mumbai")

        driver.find_element(*input_password_locator).send_keys("Bombei")
        driver.find_element(*input_confirm_password_locator).send_keys("Bombei")
        driver.find_element(*button_terms_locator).click()
        driver.find_element(*button_submit_locator).click()

        assert driver.find_element(*button_fill_again_locator).is_displayed()
        print("Тест пройден успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Закрытие браузера...")
        driver.quit()

if __name__ == "__main__":
    demo()