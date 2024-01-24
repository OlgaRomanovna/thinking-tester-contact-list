import allure
import pytest
from pages.add_contact_page import AddContactPage
from pages.login_page import LoginPage
from utils.const import BLOCKER


@allure.id("29429")
@allure.severity(BLOCKER)
@allure.title('Добавление контакта')
@pytest.mark.web
@pytest.mark.contact
def test_add_contact(open_browser):
    login_page = LoginPage()
    login_page.open()
    login_page.fill_form()
    login_page.submit()

    page = AddContactPage()
    page.open()
    page.fill_form()
    page.submit()
    page.check_result()
