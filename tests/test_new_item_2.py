import random
import string

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from conftest import browser

t_types = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder", "Multibranch Pipeline",
           "Organization Folder"]


def navigate_to_new_item_page(driver: WebDriver):
    driver.find_element(By.XPATH, "//a[contains(@href, 'newJob')]").click()


@pytest.mark.parametrize('types', t_types)
def test_new_item(browser, types):
    random_name = "item" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    wait = WebDriverWait(browser, 5)

    navigate_to_new_item_page(browser)
    wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(random_name)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='label' and text()='{types}']"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "ok-button"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@id='general']")))
    wait.until(EC.element_to_be_clickable((By.ID, 'jenkins-head-icon'))).click()

    wait.until(EC.visibility_of_element_located((By.ID, 'jenkins-head-icon')))
    result = browser.find_element(By.XPATH,
                                  f"//a[@class='jenkins-table__link model-link inside']/span[text()='{random_name}']").text

    assert random_name == result
