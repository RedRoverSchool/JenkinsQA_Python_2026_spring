import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_treugolnik(browser):
    browser.get("https://playground.learnqa.ru/puzzle/triangle")
    assert 'LearnQA - Playground' in browser.title
    side_a = browser.find_element(By.CLASS_NAME,'js_a')
    side_a.clear()
    side_a.send_keys('5')
    side_b = browser.find_element(By.CLASS_NAME,'js_b')
    side_b.clear()
    side_b.send_keys('3')
    side_c = browser.find_element(By.CLASS_NAME,'js_c')
    side_c.clear()
    side_c.send_keys('4')
    time.sleep(10)
    browser.find_element(By.XPATH,'//*[@id="puzzle"]/div[2]/div[2]/div[6]/button[1]').click()
    wait = WebDriverWait(browser, 10)
    result_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".info")))
    print(result_element.text)
    assert 'Это прямоугольный треугольник.' in result_element.text


