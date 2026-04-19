from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_w3school():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/")


    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fast-cmp-iframe"))
        )
        driver.switch_to.frame(iframe)

        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fast-cmp-button-primary[value='all']"))
        )
        accept_button.click()

        driver.switch_to.default_content()

        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.ID, "fast-cmp-iframe"))
        )
    except Exception as e:
        print(f"Ошибка при обработке iframe: {e}")

    search_field = driver.find_element(by=By.CSS_SELECTOR, value="[placeholder='Search our tutorials, e.g. HTML']")
    search_field.send_keys("Python")

    search_button = driver.find_element(by=By.ID, value="learntocode_searchbtn")
    search_button.click()


    driver.quit()

