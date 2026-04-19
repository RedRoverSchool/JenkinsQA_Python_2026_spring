from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drag_and_drop_yb(browser):
    browser.get("https://www.automationtesting.co.uk/actions.html")

    browser.find_element(By.ID, "content")

    drag_element = browser.find_element(By.ID, "dragtarget")
    drop_target = browser.find_element(By.XPATH, "(//div[@class='droptarget'])[2]")

    ActionChains(browser).drag_and_drop(drag_element, drop_target).perform()

    wait = WebDriverWait(browser, 5)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "(//div[@class='droptarget'])[2]"),
            "Drag me!"
        )
    )
    assert drop_target.text.strip() == "Drag me!"