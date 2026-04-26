from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
Test ID: TC_02.008.01
Story: US_02.008 - Save or Apply
"""

def test_freestyle_save_config(browser):
    project_name = "TC_Save_01"
    description_text = "This test is for Save button validation"

    browser.find_element(By.XPATH, "//a[@href='/view/all/newJob']").click()
    browser.find_element(By.ID, "name").send_keys(project_name)
    browser.find_element(By.CLASS_NAME, "hudson_model_FreeStyleProject").click()
    ok_button = browser.find_element(By.ID, "ok-button")
    ok_button.click()

    description_field = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.NAME, "description")))
    description_field.clear()
    description_field.send_keys(description_text)


    save_button = browser.find_element(By.NAME, "Submit")
    save_button.click()

    WebDriverWait(browser, 15).until(EC.url_contains(f"/job/{project_name}/"))
    assert f"/job/{project_name}/" in browser.current_url

    description_box = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "description")))

    assert description_box.text.strip() == description_text, \
        f"Description mismatch! Expected: {description_text}, Actual: {description_box.text}"

    assert description_text in browser.page_source

    error_el = browser.find_elements(By.CLASS_NAME, "error")
    assert len(error_el) == 0, f"Errors found: {len(error_el)}"





