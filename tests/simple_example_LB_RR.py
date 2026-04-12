from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-password")
text_box.send_keys("Selenium123**")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

print(text)

driver.quit()
