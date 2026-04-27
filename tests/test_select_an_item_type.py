import random
import string
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

types = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder", "Multibranch Pipeline",
         "Organization Folder"]
choose_type_locator = lambda item_type: (By.XPATH, f"//div[./label[text()='{item_type}']]/input")


def set_type(browser, types):
    for type in types:
        browser.find_element(*choose_type_locator(item_type=type)).click()


def preconditions(browser):
    browser.find_element(By.XPATH, "//a[contains(@href, 'newJob')]").click()


def test_select_an_item_type(browser):
    random_name = "folder_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    wait = WebDriverWait(browser, 5)

    preconditions(browser)
    wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(random_name)
    # set_type(browser, types)
    sleep(5)
