from selenium.webdriver.common.by import By

def test_saucedemo_login(browser):
    browser.get("https://www.saucedemo.com/")

    logins_list = [login for login in browser.find_element(By.ID,
                            "login_credentials").text.split() if "_user" in login]
    password = "".join([password for password in browser.find_element(By.XPATH,
                            "//div[@class='login_password']").text.split() if "sauce" in password])

    browser.find_element(By.ID, "user-name").send_keys(logins_list[0])
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    assert browser.find_element(By.XPATH, "//span[@class='title']").text == "Products"