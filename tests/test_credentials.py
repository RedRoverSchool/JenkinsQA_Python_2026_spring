import pytest

from pages.home_page import HomePage

USERNAME = "Name"
PASSWORD = "Password"
DESCRIPTION = "Description: credential type is 'Username with password'"
CREDENTIAL_ID = "1"


@pytest.mark.dependency()
def test_create(browser):
    credentials_page = (
        HomePage(browser)
        .click_manage_gear()
        .credentials_click()
        .click_add_credentials_button()
        .select_username_with_password_type()
        .click_next_button()
        .fill_credential_form(
            USERNAME,
            PASSWORD,
            CREDENTIAL_ID,
            DESCRIPTION)
        .click_submit_button()
    )

    assert credentials_page.is_credential_present(
        username=USERNAME,
        description=DESCRIPTION,
        credential_id=CREDENTIAL_ID
    ), "Credential card was not found or not visible"


@pytest.mark.dependency(depends=["test_create"])
def test_delete(browser):
    credentials_page = (
        HomePage(browser)
        .click_manage_gear()
        .credentials_click()
        .open_actions_menu()
        .click_delete()
        .cancel_delete()
        .open_actions_menu()
        .click_delete()
        .confirm_delete()
    )

    assert credentials_page.is_empty_message_visible(), (
        "Empty domain message not displayed after deletion")

    assert not credentials_page.is_credential_present(
        username=USERNAME,
        description=DESCRIPTION,
        credential_id=CREDENTIAL_ID
    ), "Credential still exists after deletion"


def test_add_credentials_ssh_username(browser):
    credential_cards = (
        HomePage(browser)
        .click_manage_gear()
        .credentials_click()
        .click_add_credentials_button()
        .select_ssh_username_with_private_key()
        .click_next_button()
        .select_system_in_add_ssh_username()
        .set_id("testID")
        .set_description("testDescription")
        .set_username("testUsername")
        .select_checkbox_treat_username_as_secret()
        .select_radiobutton_enter_directly()
        .click_add_in_privet_key()
        .set_privet_key("testKey")
        .set_passphrase("testPassphrase")
        .click_submit_button()
        .get_credentials_card()
    )

    assert any("testID" in card.text for card in credential_cards)
