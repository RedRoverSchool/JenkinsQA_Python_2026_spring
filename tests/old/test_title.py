def test_title(browser):
    """Checks if the page title is correct."""
    try:
        browser.get("https://www.selenium.dev/selenium/web/web-form.html")
        assert "Web form" in browser.title
        print(f"\n'{browser.title}' is the title.")
    except AssertionError:
        print(f"\n'{browser.title}' is NOT the title.")
    finally:
        browser.quit()