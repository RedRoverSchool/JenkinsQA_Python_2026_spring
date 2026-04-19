
from selenium import webdriver

def test_open_site():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")

    assert "Python" in driver.title


    driver.quit()


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://vk.com")
    print(driver.title)

    driver.get("https://ya.ru")
    print(driver.title)

    driver.back()
    assert "vk" in driver.current_url

    driver.refresh()

    print(driver.current_url)

    old_url = driver.current_url

    driver.forward()
    assert driver.current_url != old_url

    driver.quit()

def test_in_browser(browser):
    browser.get("https://python.org")
    assert "Python" in browser.title and "python.org" in browser.current_url
