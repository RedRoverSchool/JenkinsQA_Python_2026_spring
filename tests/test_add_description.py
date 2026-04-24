import pytest

@pytest.mark.skip(reason="Flaky test in CI - stale element")

def test_add_description(browser):
    add_button = browser.find_element(By.CSS_SELECTOR, '#description-link.jenkins-button')
    add_button.click()
    input_description = browser.find_element(By.NAME, 'description')
    input_description.send_keys('My First Jenkins Test')
    sleep(1)
    save_button = browser.find_element(By.NAME, 'Submit')
    save_button.click()
    result = browser.find_element(By.ID, 'description-content')
    assert result.text == 'My First Jenkins Test'