import os

import pytest
from selenium import webdriver

from common.jenkins_utils import login, logout, clear_data
from common.project_utils import get_browser, get_options, get_url


@pytest.fixture(scope="function")
def browser():
    get_browser()
    clear_data()

    options = webdriver.ChromeOptions()
    for option in get_options():
        options.add_argument(option)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    driver.get(get_url())
    login(driver)
    try:
        yield driver
    finally:
        try:
            logout(driver)
        finally:
            driver.quit()
