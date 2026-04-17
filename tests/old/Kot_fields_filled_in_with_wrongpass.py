import time  #added for using time.sleep()
from selenium import webdriver
from selenium.webdriver.common.by import By

def fields_filled_in_with_wrongpass():
    #drivers setting up and the page is opened
    driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    title = driver.title

    driver.implicitly_wait(0.5)

    #login filled in
    username_text_box = driver.find_element(by=By.NAME, value="username")
    username_text_box.send_keys("student")

    # password filled in
    password_text_box = driver.find_element(by=By.NAME, value="password")
    password_text_box.send_keys("12345678")


    #submission button pressed
    submit_button = driver.find_element(by=By.ID, value="submit")
    submit_button.click()

    #waiting for redirection
    time.sleep(2)

    #finding error message
    error_element = driver.find_element(By.ID, "error")

    #check the error message

    actual_error_message = error_element.text
    expected_error_message = "Your password is invalid!"

    if actual_error_message == expected_error_message:
            print("Test Passed: Correct error message displayed.")

    else:
            print(f"Test Failed: Unexpected error message: {expected_error_message}")

    driver.quit()

#start test (call the function in the beginning "def")
fields_filled_in_with_wrongpass()