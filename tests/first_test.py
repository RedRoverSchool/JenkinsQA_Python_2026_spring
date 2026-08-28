from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")

print(driver.title)

driver.quit()