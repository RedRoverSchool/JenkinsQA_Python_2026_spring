import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.skip
def test_new_item_configure_page(browser):
    wait = WebDriverWait(browser, 10)

    new_item_link = (By.XPATH, '//a[@href="/view/all/newJob"]')
    wait.until(EC.visibility_of_element_located(new_item_link)).click()

    item_name_input = (By.XPATH, '//input[@id="name"]')
    wait.until(EC.visibility_of_element_located(item_name_input)).send_keys("my_first_project")
    entered_name = browser.find_element(By.XPATH, '//input[@id="name"]').get_attribute("value")

    freestyle_project_radio = (By.XPATH, '//li[@class ="hudson_model_FreeStyleProject"]')
    wait.until(EC.visibility_of_element_located(freestyle_project_radio)).click()

    ok_button = (By.XPATH, '//button[@id="ok-button"]')
    wait.until(EC.element_to_be_clickable(ok_button)).click()

    configure_page_heading = (By.XPATH, '//h1')
    h1_text_configure_page = wait.until(EC.visibility_of_element_located(configure_page_heading)).text

    assert 'Configure' in h1_text_configure_page, 'Configure page heading does not match expected h1-text'
    assert browser.current_url == f"http://localhost:8080/job/{entered_name}/configure", "Configure page URL does not match expected url"


