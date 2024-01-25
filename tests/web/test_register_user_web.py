import allure
import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.register_page import RegisterPage
from utils.const import BLOCKER, MINOR


@allure.id("29434")
@allure.severity(BLOCKER)
@allure.title('Успешная регистрация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_positive_register(open_browser):
    login_page = LoginPage()
    login_page.open()
    register_page = RegisterPage()
    register_page.open()
    register_page.fill_form()
    register_page.submit()
    register_page.check_after_positive_register('Contact List')


@allure.id("29435")
@allure.severity(BLOCKER)
@allure.title('Безуспешная регистрация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_negative_register(open_browser):
    login_page = LoginPage()
    login_page.open()
    register_page = RegisterPage()
    register_page.open()
    register_page.submit()
    register_page.check_after_negative_register('User validation failed: firstName: Path `firstName` is required., '
                                                'lastName: Path `lastName` is required., email: Email is invalid, '
                                                'password: Path `password` is required.')


@allure.id("29436")
@allure.severity(MINOR)
@allure.title('Отмена регистрации пользователя')
@pytest.mark.web
@pytest.mark.user
def test_cancel_register(open_browser):
    login_page = LoginPage()
    login_page.open()
    register_page = RegisterPage()
    register_page.open()
    register_page.cancel()
    logout_page = LogoutPage()
    logout_page.check_result_after_log_out(
        header='Contact List App',
        sub_header='Welcome! This application is for testing purposes only. '
                   'The database will be purged as needed to keep costs down.',
        href='here'
    )
