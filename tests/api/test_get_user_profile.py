import os
import allure
import pytest
from schemas.schema_user import User
from tests.api.conftest import get_request, check_response_list_schema
from utils.const import OK, BLOCKER, CRITICAL


@allure.id("29423")
@allure.severity(BLOCKER)
@allure.title('Валидация данных пользователя после авторизации')
@pytest.mark.test_api
@pytest.mark.user
def test_get_user_profile(load_env):
    with allure.step('Получаем информацию по профилю пользователя'):
        response = get_request('/users/me')
    with allure.step('Валидируем код ответа сервера'):
        assert response.status_code == OK
    with allure.step('Валидируем ответ сервера'):
        assert response.json()['firstName'] == os.getenv('FIRST_NAME')
        assert response.json()['lastName'] == os.getenv('LAST_NAME')
        assert response.json()['email'] == os.getenv('EMAIL')
    with allure.step('Валидируем json_schema'):
        check_response_list_schema(User, response.json())



