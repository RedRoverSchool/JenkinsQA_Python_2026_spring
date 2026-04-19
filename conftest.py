import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


if not load_dotenv():
    raise FileNotFoundError("Ошибка: Файл .env не найден! Убедитесь, что он существует в корне проекта.")


@pytest.fixture(scope="session")
def chrome_options() -> list[str]:
    options = [
        "--disable-blink-features=AutomationControlled",
        "--disable-infobars",
        "--disable-notifications",
        "--password-store=basic",
        "--use-mock-keychain",
    ]
    env_options = os.getenv("BROWSER_OPTIONS_CHROME", "")
    if env_options:
        options.extend([opt.strip() for opt in env_options.split(";") if opt.strip()])
    return options


@pytest.fixture(scope="session")
def jenkins_base_url() -> str:
    return f"http://{os.getenv("JENKINS_HOST")}:{os.getenv("JENKINS_PORT")}/"


@pytest.fixture(scope="session")
def jenkins_username() -> str | None:
    return os.getenv("JENKINS_USERNAME")


@pytest.fixture(scope="session")
def jenkins_password() -> str | None:
    return os.getenv("JENKINS_PASSWORD")


@pytest.fixture(scope="session")
def jenkins_api_token() -> str | None:
    return os.getenv("JENKINS_API_TOKEN")


@pytest.fixture(scope="function")
def browser(jenkins_base_url, chrome_options, jenkins_username, jenkins_password):
    browser_name = os.getenv("BROWSER_NAME")
    if browser_name != "chrome":
        raise ValueError(f"Unsupported browser '{browser_name}'. Only 'chrome' is supported.")

    options = webdriver.ChromeOptions()
    for option in chrome_options:
        options.add_argument(option)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    driver.get(jenkins_base_url)
    driver.find_element(By.NAME, "j_username").send_keys(jenkins_username)
    driver.find_element(By.NAME, "j_password").send_keys(jenkins_password)
    driver.find_element(By.NAME, "Submit").click()

    yield driver

    driver.quit()
