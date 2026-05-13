from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create(browser):
    item_name = "test-pipeline"
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "New Item"))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "name"))
    ).send_keys(item_name)

    multibranch = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Multibranch Pipeline']")
        )
    )
    browser.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        multibranch
    )

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(multibranch)
    ).click()

    browser.find_element(By.ID, "ok-button").click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.NAME, "Submit")
        )
    ).click()

    actual_project_name = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//span[contains(text(),'{item_name}')]")
        )
    )

    assert actual_project_name.text == item_name