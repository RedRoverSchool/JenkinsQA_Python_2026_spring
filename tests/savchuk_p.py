import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver

input_name_locator = (By.XPATH, "//input[@id='firstName']")
input_last_name_locator = (By.XPATH, "//input[@id='lastName']")
input_email_locator = (By.XPATH, "//input[@id='userEmail']")
radio_button_gender_locator = lambda gender: (
    By.XPATH,
    f"//input[@type='radio' and @value='{gender}']",
)
input_phone_number = (By.XPATH, "//input[@id='userNumber']")
input_calendar = (By.XPATH, "//input[@id='dateOfBirthInput']")
select_list_moth = lambda month: (By.XPATH, f"//option[contains(text(), '{month}')]")
select_list_year = lambda year: (By.XPATH, f"//option[contains(text(), '{year}')]")
input_subjects = (By.XPATH, "//input[@id='subjectsInput']")
select_list_subjects = (
    By.XPATH,
    "//div[@role='option' and contains(text(), Economics)]",
)
checkbox_hobbies_locator = lambda hobby: (
    By.XPATH,
    f"//div[./label[text()='{hobby}']]/input",
)
input_file = (By.XPATH, "//input[@type='file']")
textarea_current_address = (By.XPATH, "//textarea[@id='currentAddress']")
select_state = (By.XPATH, "//div[@id='state']")
select_state_list = (By.XPATH, "//div[@role='option' and contains(text(), 'Haryana')]")
select_city = (By.XPATH, "//div[@id='city']")
select_city_list = (By.XPATH, "//div[@role='option' and contains(text(), 'Panipat')]")
button_submit = (By.XPATH, "//button[@type='submit']")

t_hobbies = ["Sports", "Reading", "Music"]

case_1 = {
    "first_name": "Павел",
}


def set_hobbies(driver: WebDriver, hobbies: list[str]):
    """
    Устанавливает чек-боксы хобби студента
    :param driver: WebDriver
    :param hobbies: ["Sports", "Reading", "Music"]
    :return: None
    """
    for hobby in hobbies:
        driver.find_element(*checkbox_hobbies_locator(hobby=hobby)).click()


def main():
    print("Инициализация браузера Chrome...")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-extensions")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Открытие страницы
        print(
            "Открытие тестовой страницы (https://demoqa.com/automation-practice-form)..."
        )
        driver.get("https://demoqa.com/automation-practice-form")
        driver.find_element(*input_name_locator).send_keys("Павел")
        driver.find_element(*input_last_name_locator).send_keys("Савчук")
        driver.find_element(*input_email_locator).send_keys("sdkj123fh234@mail.com")
        driver.find_element(*radio_button_gender_locator(gender="Other")).click()
        driver.find_element(*input_phone_number).send_keys("89451872360")
        driver.find_element(*input_calendar).click()
        driver.find_element(*select_list_moth(month="January")).click()
        driver.find_element(*select_list_year(year=2000)).click()
        driver.find_element(*input_calendar).send_keys(Keys.ENTER)
        # driver.find_element(*checkbox_hobbies_locator(hobby="Reading")).click()
        driver.find_element(*input_subjects).send_keys("Ec")
        time.sleep(1)
        driver.find_element(*select_list_subjects).click()
        time.sleep(1)
        set_hobbies(driver=driver, hobbies=t_hobbies)
        driver.find_element(*input_file).send_keys(r"C:\cat.jpg")
        driver.find_element(*textarea_current_address).send_keys(
            r"Казань ул. Ямашева 20 кв 2"
        )
        driver.find_element(*select_state).click()
        driver.find_element(*select_state_list).click()
        driver.find_element(*select_city).click()
        driver.find_element(*select_city_list).click()
        driver.find_element(*button_submit).click()
        time.sleep(5)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Закрытие браузера...")
        driver.quit()


if __name__ == "__main__":
    main()
