import json
import logging
import os
import allure
import pytest
import requests
from allure_commons.types import AttachmentType
from curlify import to_curl
from dotenv import load_dotenv
from requests import request
from pydantic import BaseModel


BASE_URL = 'https://thinking-tester-contact-list.herokuapp.com'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def get_curl(response, **kwargs):
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")
    allure.attach(body=str(response.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=response.url, name="API URL", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(kwargs, indent=4, ensure_ascii=True), name="Request body",
                  attachment_type=AttachmentType.JSON, extension="json")

    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body.decode('utf-8'))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


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