from selenium.webdriver.common.by import By

def test_python_org_title(browser):
    browser.get("https://www.python.org/")
    assert "Python" in browser.title