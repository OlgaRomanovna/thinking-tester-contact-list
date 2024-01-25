import allure
import pytest
from tests.api.conftest import post_request, get_token, get_request_with_invalid_token
from utils.const import OK, UNAUTHORIZED, CRITICAL


@allure.id("29420")
@allure.severity(CRITICAL)
@allure.title('Проверка код ответа сервера после деавторизации')
@pytest.mark.api
@pytest.mark.user
def test_log_out():
    with allure.step('Осуществляем logout'):
        response = post_request('/users/logout', None)
    with allure.step('Проверяем код ответа сервера'):
        assert response.status_code == OK, f'{response.status_code} is not {OK}'


@allure.id("29424")
@allure.severity(CRITICAL)
@allure.title('Проверка получения данных пользователя, для которого выполнена деавторизация')
@pytest.mark.api
@pytest.mark.user
def test_log_out_and_get_user_data():
    token = get_token()
    with allure.step('Осуществляем logout'):
        post_request('/users/logout', None)
    with allure.step('Получаем данные пользователя с истекшим токеном'):
        assert get_request_with_invalid_token('/users/me',
                                              {"Authorization": f"Bearer {token}"}).status_code == UNAUTHORIZED
