import allure
import pytest
from data import data
from tests.api.conftest import put_request
from utils.const import OK, BLOCKER


@allure.id("29425")
@allure.severity(BLOCKER)
@allure.title('Валидация кода и ответа сервера после частичной замены данных контакта')
@pytest.mark.test_api
@pytest.mark.contact
@pytest.mark.skip
def test_full_update_contact():
    json = {
        "firstName": "new_Alexander",
        "lastName": "new_Pushkin",
        "birthdate": "1799-07-07",
        "email": "new_alexander_pushkin@gmail.com",
        "phone": "8005555556",
        "street1": "new_street Glinka",
        "street2": "new_house 5, flat 17",
        "city": "new_Moscow",
        "stateProvince": "newRU",
        "postalCode": "1234567",
        "country": "new_Russia"
    }
    with allure.step('Меняем данные контакта'):
        response = put_request('/contacts/', json)
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == OK
    with allure.step('Валидируем данные контакта'):
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
