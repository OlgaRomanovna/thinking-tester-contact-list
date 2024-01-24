import json
import logging
from json import JSONDecodeError

import allure
from allure_commons.types import AttachmentType
from requests import Response
from curlify import to_curl


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def allure_logger(function):
    def wrapper(session_obj, method, url, *args, **kwargs):
        with allure.step(f"{method} {url}"):
            response: Response = function(session_obj, method, url, *args, **kwargs)

            allure.attach(
                body=to_curl(response.request).encode("utf8"),
                name=f"Request {response.status_code}",
                attachment_type=AttachmentType.TEXT,
                extension=".txt"
            )
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=4).encode("utf8"),
                    name=f"Response {response.status_code}",
                    attachment_type=AttachmentType.JSON,
                    extension=".json"
                )
            except JSONDecodeError:
                allure.attach(
                    body=response.text.encode("utf8"),
                    name=f"Response {response.status_code}",
                    attachment_type=AttachmentType.TEXT,
                    extension=".txt"
                )

        return response
    return wrapper


def logs_of_requests_in_console(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        logging.info(f'{response.status_code} {to_curl(response.request)} {response.elapsed}')

        return response
    return wrapper

