import time
from selenium.webdriver.common.by import By

items = ["Pipeline", "Freestyle project", "Multi-configuration project", "Folder",
         "Multibranch Pipeline", "Organization Folder"]

def test_new_items(browser):
    for item_name in items:
        browser.find_element(By.XPATH, '//*[@href="/view/all/newJob"]').click()
        browser.find_element(By.XPATH, "//*[@id='name']").send_keys(f"{item_name}_1")
        browser.find_element(By.XPATH, f"//span[text()='{item_name}']").click()
        browser.find_element(By.XPATH, "//button[@id='ok-button']").click()
        time.sleep(1)
        browser.get("http://localhost:8081/")
        time.sleep(1)
        elements = browser.find_elements(By.ID, f"job_{item_name}_1")

        assert len(elements) > 0, f"'job_{item_name}_1' не найден!"

#удаление[работает в цикле создал-нашел-удалил]
        # item_url = item_name.replace(" ", "%20")
        # actions = ActionChains(browser)
        # parent_element = browser.find_element(By.XPATH, f"//*[@href='job/{item_url}1/']")
        # actions.move_to_element(parent_element).perform()
        # time.sleep(1)
        # browser.find_element(By.XPATH, f"//button[contains(@data-href, 'http://localhost:8081/job/{item_url}1/')]").click()
        # time.sleep(1)
        # browser.find_element(By.XPATH, "//button[contains(@href, 'doDelete')]").click()
        # time.sleep(1)
        # browser.find_element(By.XPATH, "//button[@data-id='ok']").click()
        # # find_elements (с буквой s) вернет пустой список [], а не ошибку
        # elements = browser.find_elements(By.XPATH, f"//*[@id='job_{item_name}1']")
        #
        # assert len(elements) == 0, f"Ошибка: {item_name}1 всё еще существует!"
