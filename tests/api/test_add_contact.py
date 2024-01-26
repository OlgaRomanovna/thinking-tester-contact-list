import allure
import pytest
from schemas.schema_contacts import ModelItem
from thinking_tester_contact_list_tests.data import data
from thinking_tester_contact_list_tests.utils.const import CREATED, BLOCKER
from tests.api.conftest import post_request, check_status_code, check_response_list_schema


@allure.id("29413")
@allure.severity(BLOCKER)
@allure.title('Валидация кода и ответа сервера после добавления контакта')
@pytest.mark.api
@pytest.mark.contact
def test_add_contact():
    with allure.step('Добавляем контакт'):
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
    with allure.step('Проверяем код ответа сервера'):
        check_status_code(response, CREATED)
    json = response.json()
    with allure.step('Проверяем ответ сервера'):
        assert data.first_name == json['firstName']
        assert data.last_name == json['lastName']
        assert data.birthdate == json['birthdate']
        assert data.email == json['email']
        assert data.phone == json['phone']
        assert data.street1 == json['street1']
        assert data.street2 == json['street2']
        assert data.city == json['city']
        assert data.state_province == json['stateProvince']
        assert data.postal_code == json['postalCode']
        assert data.country == json['country']
    with allure.step('Валидируем json_schema'):
        check_response_list_schema(ModelItem, response.json())

