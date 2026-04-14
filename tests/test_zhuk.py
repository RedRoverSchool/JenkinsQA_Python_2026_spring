import time
from time import sleep
from selenium.webdriver.common.by import By

def test_search(browser):
    driver=browser
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    search_modul = driver.find_element(by=By.ID, value="p-search")
    search_child = search_modul.find_elements(by=By.XPATH, value="./*")
    assert len(search_child) == 2

    search_a = search_modul.find_element(by=By.XPATH, value="./a")
    search_d = search_modul.find_element(by=By.XPATH, value="./div")
    assert search_a in search_child
    assert search_d in search_child

    if search_a.is_displayed():
        search_a.click()
    assert search_a.is_displayed() == False
    assert search_d.is_displayed()

    search_text_box = search_d.find_element(by=By.TAG_NAME, value="input")
    assert search_text_box.is_displayed()

    search_text_box.send_keys("Koko")
    assert search_text_box.is_displayed()

    search_button = search_modul.find_element(by=By.CSS_SELECTOR, value="#searchform > div > button")
    assert search_button.is_displayed()

    search_button.click()
    sleep(2)
    new_title = driver.title
    assert new_title.find('Koko')!=-1