from selenium.webdriver.common.by import By

def click_notification_button(browser_instance):
    '''функция находит и кликает на кнопку уведомления'''

    browser_instance.get(url='https://lms.threadqa.ru/xpath-practice-hub')
    notification_button = browser_instance.find_element(by=By.CSS_SELECTOR, value='button#show-alert-btn')
    notification_button.click()



def test_check_default_text_on_notification_button(browser):
    '''тест проверяет корректность текста и присутствие значка колокольчика на кнопке уведомления после загрузки страницы'''
    browser.get(url='https://lms.threadqa.ru/xpath-practice-hub')

    assert browser.find_element(by=By.CSS_SELECTOR, value='button#show-alert-btn').text == 'Показать уведомление'
    assert browser.find_element(by=By.CSS_SELECTOR, value='button#show-alert-btn path:nth-child(1)').is_displayed()


def test_show_notification_field_after_click(browser):
    '''тест проверяет появление уведомления и корректность текста уведомления'''

    click_notification_button(browser)
    notification_field_message = browser.find_element(by=By.CSS_SELECTOR, value='div.mt-3.p-4[role="alert"] p.text-slate-300')
    notification_field_title = browser.find_element(by=By.CSS_SELECTOR, value='div.mt-3.p-4[role="alert"] h4')

    expected_message_text= 'Это важное уведомление для пользователя. Оно может содержать различную информацию.'
    assert notification_field_message.text == expected_message_text
    assert notification_field_title.text == 'Информационное сообщение'

def test_change_notification_button_text_after_click(browser):
    '''тест проверяет изменение текста на кнопке уведомления после нажатия на кнопку'''

    click_notification_button(browser)
    assert browser.find_element(by=By.CSS_SELECTOR, value='button#show-alert-btn').text == 'Скрыть уведомление'

def test_bell_picture_match_on_notification_button_and_notification_field_after_click(browser):
    '''тест проверяет совпадение значков колокола на кнопке и в поле уведомления'''

    click_notification_button(browser)

    button_bell_source = browser.find_element(by=By.CSS_SELECTOR, value='#show-alert-btn > svg > path:nth-child(1)')
    field_bell_source = browser.find_element(by=By.CSS_SELECTOR, value='#alert-message svg > path:nth-child(1)')

    assert button_bell_source.get_attribute('d') == field_bell_source.get_attribute('d')