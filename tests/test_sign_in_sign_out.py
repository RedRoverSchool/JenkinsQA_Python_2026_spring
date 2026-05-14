import os
import pytest
from dotenv import load_dotenv

from pages.home_page import HomePage
from pages.login_page import LoginPage

load_dotenv()
USERNAME = os.getenv("JENKINS_USERNAME")
PASSWORD = os.getenv("JENKINS_PASSWORD")

@pytest.mark.dependency()
def test_sign_in(browser):
    HomePage(browser).sign_out()

    home_page = (
        LoginPage(browser)
        .login(USERNAME, PASSWORD)
    )

    assert home_page.is_jenkins_icon_visible()

@pytest.mark.dependency(depends=["test_sign_in"])
def test_sign_out(browser):
    login_page = (
        HomePage(browser)
        .sign_out()
    )

    assert login_page.get_username_field() == ""
    assert login_page.get_password_field() == ""
