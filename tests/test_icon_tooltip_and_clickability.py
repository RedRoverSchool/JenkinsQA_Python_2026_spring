from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_manage_jenkins_tooltip_and_clickability(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    actions.move_to_element(
        wait.until(
            EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction"))
        )
    ).perform()

    element = wait.until(EC.visibility_of_element_located((By.ID, "root-action-ManageJenkinsAction")))

    tooltip_text = element.get_attribute("tooltip") or element.get_attribute("title")
    cursor = element.value_of_css_property("cursor")

    actions.move_by_offset(100, 100).perform()

    wait.until(EC.element_to_be_clickable((By.ID, "root-action-ManageJenkinsAction")))

    assert tooltip_text == "Manage Jenkins"
    assert cursor == "pointer"

