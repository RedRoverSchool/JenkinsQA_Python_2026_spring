from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_text_box_output(browser):
    name = "Alice"
    email = "allmadhere@mail.com"
    current_address = "The Mad Hatter's Garden, Wonderland"
    permanent_address = "Fackham Hall, Little Woldingham, Surrey RH5 8NT, UK"
    expected_output = {
        "Name": name,
        "Email": email,
        "Current Address": current_address,
        "Permananet Address": permanent_address
    }

    browser.get("https://demoqa.com/text-box")

    browser.find_element(By.ID, "userName").send_keys(name)
    browser.find_element(By.ID, "userEmail").send_keys(email)
    browser.find_element(By.ID, "currentAddress").send_keys(current_address)
    browser.find_element(By.ID, "permanentAddress").send_keys(permanent_address)
    browser.find_element(By.ID, "submit").click()

    output_field = browser.find_element(By.ID, "output").text
    actual_output = {}
    for line in output_field.split("\n"):
        key, value = line.split(":", 1)
        actual_output[key.strip()] = value.strip()

    assert actual_output == expected_output


def test_fill_practice_form(browser):
    browser.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(browser, 5)

    browser.find_element(By.ID, "firstName").send_keys("Osa")
    browser.find_element(By.ID, "lastName").send_keys("Swensson")
    browser.find_element(By.ID, "userEmail").send_keys("catchmeifyoucan@mail.com")
    browser.find_element(By.XPATH, "//input[@value='Female']").click()
    browser.find_element(By.ID, "userNumber").send_keys("1234567890")

    browser.find_element(By.ID, "dateOfBirthInput").click()
    select_month = Select(browser.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
    select_month.select_by_visible_text("June")
    select_year = Select(browser.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
    select_year.select_by_visible_text("2000")
    browser.find_element(By.XPATH,
                         "//div[contains(@class, 'react-datepicker__day' ) and contains(text(), '15')] ").click()

    browser.find_element(By.XPATH, "//input[@class='subjects-auto-complete__input']").send_keys("G")
    browser.find_element(By.XPATH,
                         "//div[contains(@class,'subjects-auto-complete__option') and text()='Biology']").click()
    browser.find_element(By.ID, "hobbies-checkbox-2").click()
    browser.find_element(By.TAG_NAME, "textarea").send_keys("9 Royal Market Road, Jaipur 302001")

    browser.find_element(By.XPATH, "//div[text()='Select State']/../..").click()
    state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-option-2")))
    browser.execute_script("arguments[0].click();", state)
    browser.find_element(By.XPATH, "//div[text()='Select City']/../..").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Panipat']"))).click()
    browser.find_element(By.ID, "submit").click()

    modal_window_text = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))).text
    assert modal_window_text == "Thanks for submitting the form"



