from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_accordion_yul_b(browser):
    browser.get("https://www.automationtesting.co.uk/index.html")
    browser.maximize_window()
    browser.find_element(By.CSS_SELECTOR, "a[href='accordion.html']").click()

    h2 = WebDriverWait(browser, 5).until( EC.visibility_of_element_located((By.ID, "content")))

    assert h2.text.strip() == "Accordion Test"

    browser.find_element(By.XPATH, "//div[normalize-space()='Platform Portability']").click()
    a1 = browser.find_element(
        By.XPATH,
        "//div[contains(., 'Testing is a repetitive process')]"
    )
    assert "Testing is a repetitive process" in a1.text

    browser.find_element(By.XPATH, "//div[normalize-space()='Language Support']").click()
    a2 = browser.find_element(
        By.XPATH,
        "//div[contains(., 'Software is written in a number')]"
    )
    assert "Software is written in a number" in a2.text

    browser.find_element(By.XPATH, "//div[normalize-space()='Selenium Grid']").click()
    a3 = browser.find_element(
        By.XPATH,
        "//div[contains(., 'The remote control server')]"
    )
    assert "The remote control server" in a3.text