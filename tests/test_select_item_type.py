import random
import string

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

t_types = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder", "Multibranch Pipeline",
         "Organization Folder"]

def preconditions(browser):
    browser.find_element(By.XPATH, "//a[contains(@href, 'newJob')]").click()

@pytest.mark.parametrize('types', t_types)
def test_select_an_item_type(browser, types):

    random_name = "folder" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    wait = WebDriverWait(browser, 5)

    preconditions(browser)
    wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(random_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='label' and text()='{types}']"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@id='general']")))
    wait.until(EC.element_to_be_clickable((By.ID, 'jenkins-head-icon'))).click()

    result = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@class='jenkins-table__link model-link inside']/span[text()='{random_name}']"))).text

    assert random_name == result