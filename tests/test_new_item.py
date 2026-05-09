import random
import string
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

invalid_character = ['?', '*', '/', '!', '%', '$', '&', ';', ':', '@', '>']
empty_values = ['', ' ']
item_types = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder", "Multibranch Pipeline",
           "Organization Folder"]

@pytest.mark.dependency()
def test_open_new_item_page(browser):
    element = browser.find_element(By.XPATH, '//a[contains(., "New Item")]')
    element.click()
    assert "New Item" in browser.title

@pytest.mark.dependency(depends=["test_open_new_item_page"])
@pytest.mark.parametrize("input_invalid_char", invalid_character)
def test_validate_invalid_item_name(browser, input_invalid_char):
    browser.find_element(By.XPATH,'//a[contains(., "New Item")]').click()
    input_field = browser.find_element(By.XPATH,"//input[@name='name']")
    input_field.clear()
    browser.find_element(By.XPATH, "//input[@name='name']").send_keys(input_invalid_char)
    browser.find_element(By.XPATH, "//div[@id='page-body']").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='itemname-invalid']")))
    locator = "//div[@id='itemname-invalid']"
    expected = f"» ‘{input_invalid_char}’ is an unsafe character"
    result = browser.find_element(By.XPATH, locator).text
    assert expected in result

@pytest.mark.dependency(depends=["test_open_new_item_page"])
@pytest.mark.parametrize("input_empty_values", empty_values)
def test_validate_empty_values(browser, input_empty_values):
    browser.find_element(By.XPATH, '//a[contains(., "New Item")]').click()
    input_field = browser.find_element(By.XPATH, "//input[@name='name']")
    input_field.clear()
    browser.find_element(By.XPATH, "//input[@name='name']").send_keys(input_empty_values)
    browser.find_element(By.XPATH, "//div[@id='page-body']").click()
    WebDriverWait(browser,10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='itemname-required']"))
    )
    locator = "//div[@id='itemname-required']"
    expected = "» This field cannot be empty, please enter a valid name"
    result = browser.find_element(By.XPATH, locator).text
    assert expected in result

@pytest.mark.dependency(depends=["test_open_new_item_page"])
@pytest.mark.parametrize("input_item_types", item_types)
def test_create_new_item(browser, input_item_types):
    random_name = "item" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    browser.find_element(By.XPATH, '//a[contains(., "New Item")]').click()
    input_field = browser.find_element(By.XPATH, "//input[@name='name']")
    input_field.clear()
    WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(random_name)
    item_type = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//span[@class='label' and text()='{input_item_types}']"))
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", item_type)
    item_type.click()
    WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH, "//h2[@id='general']")))
    WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID, 'jenkins-head-icon'))).click()
    WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.ID, 'jenkins-head-icon')))
    result = browser.find_element(By.XPATH,
                                  f"//a[@class='jenkins-table__link model-link inside']/span[text()='{random_name}']").text

    assert random_name == result
