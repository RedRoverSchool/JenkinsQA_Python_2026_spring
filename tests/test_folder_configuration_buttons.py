from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random, string

def rnd(k):
    return ''.join(random.choices(string.ascii_letters + string.digits,  k=k))

@pytest.mark.dependency
def test_create_folder(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@href="/view/all/newJob"]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='name']"))).send_keys("Folder")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Folder']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='ok-button']"))).click()
    # wait.until(EC.url_contains("/job/Folder"))
    # wait.until(EC.element_to_be_clickable((By.ID, "jenkins-head-icon"))).click()
    #
    # actions = ActionChains(browser)
    # parent_element = browser.find_element(By.XPATH, "//*[@href='job/Folder/']")
    # actions.move_to_element(parent_element).perform()
    # browser.find_element(By.XPATH, "//button[contains(@data-href, '/job/Folder/')]").click()
    # browser.find_element(By.XPATH, "//a[contains(@href, 'configure')]").click()
    # browser.find_element(By.XPATH, "//button[@data-id='ok']").click()
    # wait = WebDriverWait(browser, 10)
    # wait.until(expected_conditions.element_to_be_clickable((By.ID, "jenkins-head-icon"))).click()
    # assert пользователь на странице конфигурации

@pytest.mark.dependency(depends=["test_create_folder"])
def test_config_save(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'newJob')]")))
    browser.get("http://localhost:8080/job/Folder/configure")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="_.displayNameOrNull"]'))).send_keys(rnd(15))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@name="_.description"]'))).send_keys(rnd(50))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@name = "Submit"]'))).click()

    assert ("configure" not in browser.current_url), "Url changed, Save button redirected"

@pytest.mark.dependency(depends=["test_create_folder"])
def test_config_apply(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'newJob')]")))
    browser.get("http://localhost:8080/job/Folder/configure")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="_.displayNameOrNull"]'))).clear()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea[@name="_.description"]'))).clear()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@name="Apply"]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='notification-bar']//span[text()='Saved']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@name="Apply"]'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH , "//*[@id='notification-bar']//span[text()='Saved']")))

    assert "configure" in browser.current_url, "Apply применяется, редиректа нет"
