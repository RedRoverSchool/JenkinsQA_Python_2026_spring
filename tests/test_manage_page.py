
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# TC_10.001.01 | Manage Jenkins > Visibility and clickability > Verify navigation to manage Jenkins page
def test_verify_navigation_to_manage_page(browser):
    wait = WebDriverWait(browser, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction"))).click()

    wait.until(EC.url_contains("/manage"))

    assert "/manage" in browser.current_url


# TC_10.001.02 | Manage Jenkins > Visibility and clickability > Verify "Manage Jenkins" option is visible on Dashboard
def test_verify_icon_is_visible(browser):
    wait = WebDriverWait(browser, 10)

    assert wait.until(EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction"))).is_displayed()


# TC_10.001.03 | Manage Jenkins > Visibility and clickability > Verify "Manage Jenkins" icon tooltip and clickability on hover
def test_verify_tooltip_and_clickable(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    actions.move_to_element(
        wait.until(
            EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction"))
        )
    ).perform()

    element = wait.until(EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction")))

    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Manage Jenkins')]")))

    cursor = element.value_of_css_property("cursor")

    wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction"))).click()

    assert cursor == "pointer"



