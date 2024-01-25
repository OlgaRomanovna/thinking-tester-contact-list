import json
import os
import allure
import pytest
import logging

from allure_commons.types import AttachmentType
from curlify import to_curl
from dotenv import load_dotenv
from requests import request
from pydantic import BaseModel


BASE_URL = 'https://thinking-tester-contact-list.herokuapp.com'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def get_curl(response):
    allure.attach(
        body=to_curl(response.request).encode("utf8"),
        name=f"Request {response.status_code}",
        attachment_type=AttachmentType.TEXT,
        extension=".txt"
    )


def get_token():
    json = {"email": f"{os.getenv('EMAIL')}",
            "password": f"{os.getenv('PASSWORD_USER')}"}
    response = request("POST", f'{BASE_URL}/users/login', json=json)
    return response.json()['token']


def post_request(endpoint, json):
    response = request("POST", f'{BASE_URL}{endpoint}', json=json, headers={"Authorization": f"Bearer {get_token()}"})
    get_curl(response)
    return response


def post_request_without_token(endpoint, json):
    response = request("POST", f'{BASE_URL}{endpoint}', json=json)
    get_curl(response)
    return response


def delete_request(endpoint):
    response = request("DELETE", f'{BASE_URL}{endpoint}', headers={"Authorization": f"Bearer {get_token()}"})
    get_curl(response)
    return response


def get_request(endpoint):
    response = request("GET", f'{BASE_URL}{endpoint}', headers={"Authorization": f"Bearer {get_token()}"})
    get_curl(response)
    return response


def get_request_with_invalid_token(endpoint, header):
    response = request("GET", f'{BASE_URL}{endpoint}', headers=header)
    get_curl(response)
    return response


def put_request(endpoint, json):
    response = request("PUT", f'{BASE_URL}{endpoint}', json=json, headers={"Authorization": f"Bearer {get_token()}"})
    get_curl(response)
    return response


def check_response_list_schema(class_schemas: BaseModel, response: object) -> None:
    with allure.step('Проверка тела ответа'):
        class_schemas.parse_obj(response)


def check_status_code(response, actual):
    with allure.step('Проверяем код ответа сервера'):
        assert response.status_code == actual, f'Код ответа отличается от ожидаемого, получен {response.status_code}'