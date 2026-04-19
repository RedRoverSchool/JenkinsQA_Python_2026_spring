from selenium.webdriver.common.by import By


def test_add_to_cart(browser):
    browser.get("https://www.saucedemo.com/")

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    title_text = browser.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert title_text == "Sauce Labs Backpack"
