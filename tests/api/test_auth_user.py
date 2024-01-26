import os
import allure
import pytest
from tests.api.conftest import post_request, check_status_code
from thinking_tester_contact_list.utils.const import OK, BLOCKER


@allure.id("29411")
@allure.severity(BLOCKER)
@allure.title('Валидация данных пользователя после авторизации')
@pytest.mark.api
@pytest.mark.user
def test_auth(load_env):
    with allure.step('Выполняем авторизацию'):
        json = {"email": f"{os.getenv('EMAIL')}",
                "password": f"{os.getenv('PASSWORD_USER')}"}
        response = post_request('/users/login', json=json)
    with allure.step('Валидируем код ответа сервера'):
        check_status_code(response, OK)
