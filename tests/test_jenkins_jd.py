from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

def test_jenkins_logo(browser):
    """Проверка главного логотипа"""
    logo_url = browser.find_element(By.ID, 'jenkins-head-icon').get_dom_attribute('src')

    assert logo_url == '/static/610f94eb/images/svgs/logo.svg'

def test_new_item_page_title(browser):
    """Проверка title на NewItemPage"""
    new_item_page_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(., 'New Item')]")
        )
    )
    new_item_page_link.click()

    assert browser.title == "New Item - Jenkins"

def test_description_textarea_opening(browser):
    """Проверка возможности ввода описания"""
    add_description_btn = browser.find_element(By.ID, 'description-link')
    add_description_btn.click()

    textarea = browser.find_element(By.XPATH, "//textarea[@name='description']")

    assert textarea.is_displayed()

def test_description_text_cancelation(browser):
    """Проверка отмены ввода описания """
    add_description_btn = browser.find_element(By.ID, 'description-link')
    add_description_btn.click()

    cancel_btn = browser.find_element(By.CSS_SELECTOR, '.jenkins-button.description-cancel-button')
    cancel_btn.click()

    assert len(browser.find_elements(By.NAME, "description")) == 0

