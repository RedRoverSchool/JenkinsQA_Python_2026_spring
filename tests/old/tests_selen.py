from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/")


driver.implicitly_wait(0.5)

messages = driver.find_element(by=By.CLASS_NAME, value="fw-bold")
print(messages.text)

link = driver.find_element("xpath", "//a[span[text()='Documentation']]")
link.click()
driver.implicitly_wait(10)
title = driver.find_element(by=By.TAG_NAME, value="h1")
print(title.text)
sleep(5)
tab = driver.find_element(by=By.ID, value="tabs-03-02-tab")
tab.click()
sleep(5)


driver.quit()