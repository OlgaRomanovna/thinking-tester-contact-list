import os
import allure
import pytest

from data.data import first_name_for_register, last_name_for_register, email_for_register, password
from tests.api.conftest import post_request, delete_request, check_status_code
from utils.const import CREATED, OK, CRITICAL


@allure.id("29417")
@allure.severity(CRITICAL)
@allure.title('Проверка кода ответа от сервера после удаления пользователя')
@pytest.mark.test_api
@pytest.mark.user
@pytest.mark.skip
def test_delete_user(load_env):
    with allure.step('Регистрируем пользователя'):
        json = {
            "firstName": f"{first_name_for_register}",
            "lastName": f"{last_name_for_register}",
            "email": f"{email_for_register}",
            "password": f"{password}"
        }
        response = post_request('/users', json)
        check_status_code(response, CREATED)
    with allure.step('Удаляем пользователя'):
        response = delete_request('/users/me')
        check_status_code(response, OK)
