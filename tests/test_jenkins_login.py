def test_login_page_title(browser):




    assert browser.title is not None
    assert "Jenkins" in browser.title
    assert "login" in browser.current_url
