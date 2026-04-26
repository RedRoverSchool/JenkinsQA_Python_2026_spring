
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.skip
def test_check_the_button(browser):
    wait = WebDriverWait(browser, 10)

    new_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/view/all/newJob']")))
    new_item.click()

    button_ok = wait.until(EC.presence_of_element_located((By.ID, 'ok-button')))
    assert not button_ok.is_enabled()