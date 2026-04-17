import time  #added for using time.sleep()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def imdb_search_field():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # drivers setting up and the page is opened
    driver = webdriver.Chrome()

    driver.get("https://www.imdb.com/")
    title = driver.title
    driver.implicitly_wait(2)

    #cookies acception

    cookie_button = driver.find_element(By.CSS_SELECTOR, value = 'button[data-testid="accept-button"]')
    cookie_button.click()
    print("Cookies accepted!")

    time.sleep(5)  #the cookies window physically closed

    # search field filled in

    search_input = driver.find_element(By.ID, value= "suggestion-search")
    search_input.send_keys("Home alone")
    search_input.submit()

    time.sleep(5)

    #checking the result
    results_header = driver.find_element(By.CLASS_NAME, value="ipc-title__text")

    print("Header founded")

    if "Home alone" in driver.page_source:
        print("Search succeeded!")
    else:
        print("Search failed!")
    driver.quit()

#start test (call the function in the beginning "def")
imdb_search_field()
