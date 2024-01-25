import allure
import pytest
from schemas.schema_contacts import Model
from tests.api.conftest import get_request, check_response_list_schema
from utils.const import OK, BLOCKER, CRITICAL


@allure.id("29419")
@allure.severity(BLOCKER)
@allure.title('Валидация кода и ответа сервера после получения контакта')
@pytest.mark.test_api
@pytest.mark.contact
def test_get_contact():
    with allure.step('Получаем контакт'):
        response = get_request('/contacts/')
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == OK
    with allure.step('Валидируем json_schema'):
        check_response_list_schema(Model, response.json())


@allure.id("29421")
@allure.severity(CRITICAL)
@allure.title('Валидация кода и ответа сервера после получения списка контактов')
@pytest.mark.api
@pytest.mark.contact
def test_get_contacts():
    with allure.step('Получаем список контактов'):
        response = get_request('/contacts')
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == OK
    with allure.step('Валидируем json_schema'):
        check_response_list_schema(Model, response.json())

