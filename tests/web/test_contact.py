import allure
import pytest
from thinking_tester_contact_list.pages.add_contact_page import add_contact_page
from thinking_tester_contact_list.pages.login_page import login_page
from thinking_tester_contact_list.utils.const import BLOCKER


@allure.id("29429")
@allure.severity(BLOCKER)
@allure.title('Добавление контакта')
@pytest.mark.web
@pytest.mark.contact
def test_add_contact(open_browser):
    login_page.open()
    login_page.fill_form()
    login_page.submit()

    add_contact_page.open()
    add_contact_page.fill_form()
    add_contact_page.submit()
    add_contact_page.check_result()


