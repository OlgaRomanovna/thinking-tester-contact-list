import allure
import pytest
from thinking_tester_contact_list_tests.pages.login_page import login_page
from thinking_tester_contact_list_tests.pages.logout_page import logout_page
from thinking_tester_contact_list_tests.utils.const import BLOCKER, MINOR


@allure.id("29430")
@allure.severity(BLOCKER)
@allure.title('Авторизация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_login(open_browser):
    login_page.open()
    login_page.fill_form()
    login_page.submit()
    login_page.check_result_after_login(header='Contact List', sub_header='Click on any contact to view the Contact Details')


@allure.id("29431")
@allure.severity(BLOCKER)
@allure.title('Деавторизация пользователя')
@pytest.mark.web
@pytest.mark.user
def test_logout(open_browser):
    login_page.open()
    login_page.fill_form()
    login_page.submit()
    logout_page.log_out()
    logout_page.check_result_after_log_out(
        header='Contact List App',
        sub_header='Welcome! This application is for testing purposes only. '
                   'The database will be purged as needed to keep costs down.',
        href='here'
    )


@allure.id("29432")
@allure.severity(BLOCKER)
@allure.title('Авторизация пользователя с некорректными данными')
@pytest.mark.web
@pytest.mark.user
def test_incorrect_login(open_browser):
    login_page.open()
    login_page.fill_form_incorrect()
    login_page.submit()
    login_page.check_result_after_incorrect_login_data('Incorrect username or password')


@allure.id("29433")
@allure.severity(MINOR)
@allure.title('Проверка ссылки на главной странице')
@pytest.mark.web
def test_check_api_documentation(open_browser):
    login_page.open()
    login_page.check_link()
