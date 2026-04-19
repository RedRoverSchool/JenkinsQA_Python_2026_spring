from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


HOME_URL = "https://docs.astral.sh/uv/"
INSTALLER_URL = "https://docs.astral.sh/uv/reference/installer/"


def _first_visible_search_result(driver):
    result_links = driver.find_elements(By.CSS_SELECTOR, "a.md-search-result__link")
    visible_links = [link for link in result_links if link.is_displayed()]
    return visible_links[0] if visible_links else False


def test_uv_search_opens_installer_and_copies_command(browser):
    # E2E-сценарий:
    # открыть документацию uv, найти installer через поиск, перейти по первому результату,
    # скопировать команду установки и проверить уведомление "Copied to clipboard"
    browser.set_window_size(1400, 900)
    wait = WebDriverWait(browser, 10)

    # Шаг 1: открыть главную страницу документации uv
    browser.get(HOME_URL)

    # Шаг 2: ввести "install" в поиске
    search_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']"))
    )
    search_input.click()
    search_input.send_keys("install")

    # Шаг 3: открыть первый результат поиска с документацией по uv installer
    first_result = wait.until(_first_visible_search_result)
    assert first_result.text.strip() == "The uv installer"
    assert first_result.get_attribute("href") == INSTALLER_URL
    first_result.click()

    # Шаг 4: проверить редирект на страницу installer reference
    wait.until(EC.url_to_be(INSTALLER_URL))
    assert browser.current_url == INSTALLER_URL

    # Шаг 5: нажать кнопку копирования команды установки
    copy_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Copy to clipboard']"))
    )
    copy_button.click()

    # Шаг 6: проверить, что появилось уведомление "Copied to clipboard"
    copied_notification = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.md-dialog__inner.md-typeset")
        )
    )
    assert copied_notification.text.strip() == "Copied to clipboard"
