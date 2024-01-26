import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from thinking_tester_contact_list_tests.utils.attachments import add_html, add_screenshot, add_video, add_logs


@pytest.fixture(scope='function')
def open_browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_version = request.config.getoption('browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": f"{browser_name}",
        "browserVersion": f"{browser_version}",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = 'https://thinking-tester-contact-list.herokuapp.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    add_html(browser)
    add_screenshot(browser)
    add_video(browser)
    add_logs(browser)
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_version', action='store', default="99.0")


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


