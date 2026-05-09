import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.dependency
def test_create_freestyle_project(browser):
    wait = WebDriverWait(browser, 10)

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys("Test Freestyle")
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    browser.find_element(By.ID, "ok-button").click()

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.NAME, "Submit"))
    )
    submit_btn.click()

    assert browser.find_element(By.CSS_SELECTOR, ".job-index-headline.page-headline").text == "Test Freestyle"

@pytest.mark.dependency(depends=["test_create_freestyle_project"])
def test_description_preview(browser):
    freestyle_project = browser.find_element(By.XPATH, "//a[@href='job/Test%20Freestyle/']")
    ActionChains(browser).move_to_element(freestyle_project).perform()
    browser.find_element(By.CSS_SELECTOR, '[id="job_Test Freestyle"] .jenkins-menu-dropdown-chevron').click()
    browser.find_element(By.XPATH, "//a[@href='/job/Test%20Freestyle/configure']").click()

    description_textarea = browser.find_element(By.XPATH, "//textarea[@name='description']")
    description_textarea.send_keys("test preview")
    preview_textarea = browser.find_element(By.CLASS_NAME, "textarea-show-preview")
    preview_textarea.click()
    preview_textarea_text = browser.find_element(By.CLASS_NAME, "textarea-preview")

    assert preview_textarea.is_displayed()
    assert preview_textarea_text.text == description_textarea.get_attribute("value")
