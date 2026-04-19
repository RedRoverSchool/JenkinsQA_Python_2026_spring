from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_browser_tabs_yb(browser):
    wait = WebDriverWait(browser, 5)

    browser.get("https://www.automationtesting.co.uk/browserTabs.html")
    window1 = browser.current_window_handle

    browser.find_element(By.CSS_SELECTOR, "input[value='Open Tab']").click()

    wait.until(EC.number_of_windows_to_be(2))
    browser.switch_to.window(browser.window_handles[-1])

    wait.until(EC.url_contains("google"))
    browser.switch_to.window(window1)
    
    assert browser.current_window_handle == window1