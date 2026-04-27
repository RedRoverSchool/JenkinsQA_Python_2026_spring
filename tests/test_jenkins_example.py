import time

import pytest
from pytest_dependency import depends
from selenium.webdriver.common.by import By

@pytest.mark.dependency()
def test_welcome(browser):
    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")

    assert label.text == "Welcome to Jenkins!"

@pytest.mark.dependency()
def test_welcome2(browser):
    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")

    assert label.text == "Welcome to Jenkins!"

@pytest.mark.dependency(depends=["test_welcome", "test_welcome2"])
def test_welcome4(browser):
    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")

    assert label.text == "Welcome to Jenkins!"

@pytest.mark.dependency(depends=["test_welcome"])
def test_welcome3(browser):
    label = browser.find_element(By.CSS_SELECTOR, "div.empty-state-block > h1")

    assert label.text == "Welcome to Jenkins!"
