import os
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import data
from tests.api.conftest import post_request
from utils import const
from utils.attachments import add_html, add_screenshot, add_video, add_logs

DEFAULT_BROWSER_VERSION = '120'


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
    if browser_name == 'chrome':
        add_logs(browser)
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_version', action='store', default="99.0")


@pytest.fixture()
def add_contact_fixture():
    with allure.step('Создаём контакт'):
        json = {
            "firstName": data.first_name,
            "lastName": data.last_name,
            "birthdate": data.birthdate,
            "email": data.email,
            "phone": data.phone,
            "street1": data.street1,
            "street2": data.street2,
            "city": data.city,
            "stateProvince": data.state_province,
            "postalCode": data.postal_code,
            "country": data.country
        }
        response = post_request(f'/contacts', json=json)
        assert response.status_code == const.CREATED
        return response


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture()
def web_user_for_auth():
    return UserModel(email=os.getenv('EMAIL'), password=os.getenv('PASSWORD_USER'))


@pytest.fixture(scope='session')
def get_user_data_from_env():
    with allure.step('Получаем данные по пользователю'):
        resp = auth(email=os.getenv('EMAIL'),
                    password=os.getenv('PASSWORD_USER'))
        assert resp.status_code == const.OK
        return UserModel(token=resp.json()['token'], _id=resp.json()['user']['_id'])
