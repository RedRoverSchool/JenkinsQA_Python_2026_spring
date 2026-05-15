import pytest

from pages.home_page import HomePage


USER_NAME = "Vova"
FULL_NAME = "Vovan"


@pytest.mark.dependency()
def test_create_user(browser):

    user = (HomePage(browser)
        .manage_gear_click()
        .click_users()
        .click_create_user()
        .set_input("username", USER_NAME)
        .set_input("password1", "123")
        .set_input("password2", "123")
        .set_input("fullname", FULL_NAME)
        .set_input("email", "vova@mail.com")
        .click_create_user()
        .is_find_user_name(USER_NAME)
     )

    assert user, "Пользователь не найден"


@pytest.mark.dependency(depends=["test_create_user"])
def test_open_user_profile_page(browser):
    user = (HomePage(browser)
            .manage_gear_click()
            .click_users()
            .click_any_user()
            )

    # assert user, f"Страница пользователя {user} не доступна"

@pytest.mark.dependency(depends=["test_open_user_profile_page"])
def test_delete_user(browser):
    pass