from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_edit_description(browser):
    browser.find_element(By.ID, 'description-link').click()

    text_description = "My test description"
    browser.find_element(By.NAME, 'description').send_keys(text_description)

    browser.find_element(By.XPATH, "//*[@class='textarea-show-preview']").click()
    browser.find_element(By.XPATH, "//*[@class='textarea-hide-preview']").click()

    browser.find_element(By.NAME, 'Submit').click()

    wait = WebDriverWait(browser, 10)
    description = wait.until(EC.visibility_of_element_located((By.ID, "description-content")))

    assert description.text == text_description









