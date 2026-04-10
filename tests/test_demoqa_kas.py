from selenium.webdriver.common.by import By


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




