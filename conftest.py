import pytest
from selenium import webdriver

from common.jenkins_utils import login, logout, clear_data
from common.order_utils import reorder_items_by_dependency
from common.project_utils import get_browser, get_options, get_url


@pytest.fixture(scope="function")
def browser(request):
    get_browser()

    print(f"\n{request.node.path.name}::{request.node.name}")
    dependency_marker = request.node.get_closest_marker("dependency")
    depends = dependency_marker.kwargs.get("depends") if dependency_marker else None
    if not depends:
        print("clearing data")
        clear_data()

    options = webdriver.ChromeOptions()
    for option in get_options():
        options.add_argument(option)
    print("opening browser")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    print("getting page")
    driver.get(get_url())
    login(driver)
    try:
        yield driver
    finally:
        try:
            logout(driver)
        finally:
            driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):
    reorder_items_by_dependency(items)
