
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_navigation_to_manage_page(browser):
    wait = WebDriverWait(browser, 10)

    manage_jenkins = wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction")))
    manage_jenkins.click()

    wait.until(EC.url_contains("/manage"))

    configure_system = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'configure')]")))

    assert "/manage" in browser.current_url
    assert configure_system.is_displayed()