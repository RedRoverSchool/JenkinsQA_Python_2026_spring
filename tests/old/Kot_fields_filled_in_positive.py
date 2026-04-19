import time  #added for using time.sleep()
from selenium import webdriver
from selenium.webdriver.common.by import By

def fields_filled_in():
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
    password_text_box.send_keys("Password123")


    #submission button pressed
    submit_button = driver.find_element(by=By.ID, value="submit")
    submit_button.click()

    #waiting for redirection
    time.sleep(2)

    #check the successfull login
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    current_url = driver.current_url

    if current_url == expected_url:
        print("Logged in successfully")
    else:
        print("Login failed")

    driver.quit()

#start test (call the function in the beginning "def")
fields_filled_in()