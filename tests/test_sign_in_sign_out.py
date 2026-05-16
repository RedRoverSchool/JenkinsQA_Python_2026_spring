import os
import pytest
from dotenv import load_dotenv

from pages.home_page import HomePage
from pages.login_page import LoginPage

load_dotenv()
USERNAME = os.getenv("JENKINS_USERNAME")
PASSWORD = os.getenv("JENKINS_PASSWORD")
NOT_VALID_USERNAME = "not valid user"
NOT_VALID_PASSWORD = "any password"


@pytest.mark.dependency()
def test_sign_in(browser):
    HomePage(browser).sign_out()

    home_page = LoginPage(browser).login(USERNAME, PASSWORD)

    assert home_page.is_jenkins_icon_visible()


@pytest.mark.dependency(depends=["test_sign_in"])
def test_sign_out(browser):
    login_page = HomePage(browser).sign_out()

    assert login_page.get_username_field() == ""
    assert login_page.get_password_field() == ""


def test_sign_in_with_error(browser):
    HomePage(browser).sign_out()
    result_page = (
        LoginPage(browser)
        .set_username_field(NOT_VALID_USERNAME)
        .set_password_field(NOT_VALID_PASSWORD)
        .sign_in_button_click()
    )

    assert result_page.get_error_message() == "Invalid username or password"
