from selenium.webdriver.common.by import By
import time


def test_shkarpetki_page_title(browser):
    browser.get('https://ragna.by/')
    time.sleep(3)
    adzenne = browser.find_element(By.CSS_SELECTOR, '.cat-item-1449 .accordion-cat-toggle')
    adzenne.click()
    time.sleep(2)
    shkarpetki = browser.find_element(By.LINK_TEXT, 'Шкарпэткі')
    shkarpetki.click()
    time.sleep(2)
    assert browser.title == 'Шкарпэткі | Этнакрама РАГНА'
