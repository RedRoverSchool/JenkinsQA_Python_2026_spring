from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_description_preview(browser):
    wait = WebDriverWait(browser, 10)

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys("Test Freestyle")
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()

    button = wait.until(
        EC.element_to_be_clickable((By.ID, "ok-button"))
    )
    button.click()

    description_textarea = browser.find_element(By.XPATH, "//textarea[@name='description']")
    description_textarea.send_keys("test preview")
    preview_textarea = browser.find_element(By.CLASS_NAME, "textarea-show-preview")
    preview_textarea.click()
    preview_textarea_text = browser.find_element(By.CLASS_NAME, "textarea-preview")

    assert preview_textarea.is_displayed()
    assert preview_textarea_text.text == description_textarea.get_attribute("value")
