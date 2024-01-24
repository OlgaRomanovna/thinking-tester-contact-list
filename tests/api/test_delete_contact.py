import allure
import pytest
from tests.api.conftest import delete_request, get_request, check_status_code
from utils.const import NOT_FOUND, OK, BLOCKER


@allure.id("29414")
@allure.severity(BLOCKER)
@allure.title('Удаление контакта пользователя')
@pytest.mark.test_api
@pytest.mark.contact
def test_delete_contact():
    with allure.step('Удаляем контакт'):
        response = delete_request('/contacts/')
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == OK


@allure.id("29415")
@allure.severity(BLOCKER)
@allure.title('Удаление контакта пользователя')
@pytest.mark.test_api
@pytest.mark.contact
def test_delete_contact_and_get_deleted_contact():
    with allure.step('Удаляем контакт'):
        delete_request('/contacts/')
    with allure.step('Получение удалённого контакта'):
        response = get_request('/contacts/')
        check_status_code(response, NOT_FOUND)
