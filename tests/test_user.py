import pytest
import time
from pages.home_page import HomePage


USER_NAME = "User"
FULL_NAME = "Test User"
PASSWORD = "123"
EMAIL_USER = "user@test"


@pytest.mark.dependency()
def test_create_user(browser):

    user = (HomePage(browser)
        .click_manage_gear()
        .click_users()
        .click_create_user()
        .set_input("username", USER_NAME)
        .set_input("password1", PASSWORD)
        .set_input("password2", PASSWORD)
        .set_input("fullname", FULL_NAME)
        .set_input("email", EMAIL_USER)
        .click_create_user()
        .is_find_user_name(USER_NAME)
     )

    assert user, "Пользователь не найден"

@pytest.mark.dependency(depends=["test_create_user"])
def test_open_user_profile_page(browser):
    user = (HomePage(browser)
            .click_manage_gear()
            .click_users()
            .click_user_id(USER_NAME)
            .get_user_name()
            )

    assert USER_NAME in user, f"Страница пользователя {USER_NAME} не доступна"

@pytest.mark.dependency(depends=["test_open_user_profile_page"])
def test_delete_user(browser):
    user = (HomePage(browser)
            .click_manage_gear()
            .click_users()
            .delete_user(USER_NAME)
            .is_find_user_name(USER_NAME))

    assert user is False, "Пользователь не удалён"
