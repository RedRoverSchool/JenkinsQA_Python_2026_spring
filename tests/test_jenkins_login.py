from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_jenkins_login_page_opens():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get("http://localhost:8080/login")

    assert driver.title is not None
    assert "Jenkins" in driver.title
    assert "login" in driver.current_url

    driver.quit()