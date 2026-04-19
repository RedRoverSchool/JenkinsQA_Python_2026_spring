from selenium.webdriver.common.by import By

def test_hh(browser):
    browser.get('https://hh.ru/vacancy/132138575')
    vacancy = browser.find_element(By.CSS_SELECTOR, 'h1[data-qa="vacancy-title"]')

    assert vacancy.text == 'Тестировщик'