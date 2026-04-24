import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

freestyle_name = "Freestyle_Name"


@pytest.mark.skip(reason="Flaky test in CI - stale element")
def test_create_freestyle_project(browser):
    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(freestyle_name)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()

    browser.find_element(By.ID, "ok-button").click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class='app-jenkins-logo']"))).click()

    created_freestyle = browser.find_element(By.XPATH, f"(//a[@href='job/{freestyle_name}/'])[1]").text

    assert created_freestyle == freestyle_name
