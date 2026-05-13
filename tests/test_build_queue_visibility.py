import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_build_queue_visibility(browser):
    button = browser.find_element(By.CSS_SELECTOR, "#buildQueue > div.pane-header > a > svg")
    button.click()

    wait = WebDriverWait(browser, 10)

    wait.until(
    EC.text_to_be_present_in_element(
    (By.XPATH, "//td[@class='pane']"),
    "No builds in the queue."))

    text_element = browser.find_element(By.XPATH, "//td[@class='pane']")
    assert text_element.text == "No builds in the queue."

