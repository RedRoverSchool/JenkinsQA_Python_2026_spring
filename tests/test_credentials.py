import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

USERNAME = "Name"
PASSWORD = "Password"
DESCRIPTION = "Description: credential type is 'Username with password'"
CREDENTIAL_ID = "1"


def create_credential(driver, username, password, description, credential_id, treat_as_secret=False):
    driver.find_element(By.XPATH, "//*[@href = '/manage']").click()
    driver.find_element(By.XPATH, "//*[@href ='credentials']").click()
    driver.find_element(By.XPATH, "//button[contains(text(), 'Add Credentials')]").click()
    driver.find_element(By.XPATH, "//div[text() = 'Username with password']").click()
    driver.find_element(By.ID, "cr-dialog-next").click()

    driver.find_element(By.NAME, "_.username").send_keys(username)
    driver.find_element(By.NAME, "_.password").send_keys(password)
    driver.find_element(By.NAME, "_.description").send_keys(description)
    driver.find_element(By.NAME, "_.id").send_keys(credential_id)

    if treat_as_secret:
        checkbox = driver.find_element(By.NAME, "_.usernameSecret")
        if not checkbox.is_selected():
            checkbox.click()

    driver.find_element(By.ID, "cr-dialog-submit").click()


def navigate_to_credential_form(driver):
    driver.find_element(By.XPATH, "//*[@href = '/manage']").click()
    driver.find_element(By.XPATH, "//*[@href ='credentials']").click()
    driver.find_element(By.XPATH, "//button[contains(text(), 'Add Credentials')]").click()
    driver.find_element(By.XPATH, "//div[text() = 'Username with password']").click()
    driver.find_element(By.ID, "cr-dialog-next").click()


def find_credential_card(driver, username=None, description=None, credential_id=None, treat_as_secret=False):
    if treat_as_secret:
        card_found_by_id = f"//*[@href='credential/{credential_id}']"
        return driver.find_element(By.XPATH, card_found_by_id)
    else:
        card_found_by_username_and_description = (
            f'(//div[contains(@class, "credentials-card")]'
            f'[.//span[contains(text(),"{username}/******")]]'
            f'[.//span[contains(text(),"{description}")]])[1]'
        )
        return driver.find_element(By.XPATH, card_found_by_username_and_description)


@pytest.mark.dependency()
def test_create(browser):
    create_credential(browser, USERNAME, PASSWORD, DESCRIPTION, CREDENTIAL_ID, treat_as_secret=False)

    credential_card = find_credential_card(
        browser,
        username=USERNAME,
        description=DESCRIPTION,
        credential_id=CREDENTIAL_ID,
        treat_as_secret=False
    )

    assert credential_card.is_displayed(), "Credential card was not found or not visible"


@pytest.mark.dependency(depends=["test_create"])
def test_create_duplicate_id_error_validation(browser):
    expected_error = "This ID is already in use"

    navigate_to_credential_form(browser)

    id_field = browser.find_element(By.NAME, "_.id")
    id_field.send_keys(CREDENTIAL_ID)
    browser.execute_script("arguments[0].blur();", id_field)

    actual_error = WebDriverWait(browser, 10).until(
        lambda d: d.find_element(By.XPATH, "//div[@class='error']").text
    )

    assert actual_error == expected_error
