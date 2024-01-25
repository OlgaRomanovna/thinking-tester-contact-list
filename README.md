# QA Guru: Дипломный проект
Реализация набора автотестов (UI, API) для сервиса <code>thinking-tester-contact-list.herokuapp</code>

Проект реализован с использованием:

<img src="resources/icons/python-original.svg" width="50"> <img src="resources/icons/pytest.png" width="50"> <img src="resources/icons/intellij_pycharm.png" width="50"> <img src="resources/icons/selene.png" width="50"> <img src="resources/icons/selenium.png" width="50"> <img src="resources/icons/selenoid.png" width="50"> <img src="resources/icons/jenkins.png" width="50"> <img src="resources/icons/allure_report.png" width="50"> <img src="resources/icons/allure_testops.png" width="50"> <img src="resources/icons/tg.png" width="50"> <img src="resources/icons/jira.png" width="50">

Запуск тестов и формирование отчетов о запусках формируется с помощью:
 - <code>Jenkins;</code>
 - <code>Selenoid;</code>
 - <code>Allure TestOps.</code>

# Покрытый функционал

## <a href='https://github.com/OlgaRomanovna/qa_guru_diploma/tree/main/web'>UI-тесты</a>
 - авторизация пользователя;
 - добавление контакта в список контактов пользователя;
 - выход из учетной записи.

## <a href='https://github.com/OlgaRomanovna/qa_guru_diploma/tree/main/api'>API-тесты</a>
 - получение профиля пользователя;
 - регистрация пользователя;
 - удаление пользователя;
 - авторизация пользователя;
 - выход из учётной записи;
 - добавление контакта в список контактов пользователя;
 - получение информации о контакте;
 - частичное обновление информации о контакте;
 - полное обновление информации о контакте;
 - удаление контакта пользователя.

## Подготовка перед запуском
- создать файл с данными уже существующего пользователя;
- создать файл с данными об удалённом сервере selenoid;
- создать файл с данным об телеграм-боте, куда необходимо отправить данные о прохождении тестов.

## Полезные ссылки
 - [Тестируемое web-приложение](https://thinking-tester-contact-list.herokuapp.com/);
 - [Job Jenkins](https://jenkins.autotests.cloud/job/oromanovna_diploma/);
 - [Allure report](https://jenkins.autotests.cloud/job/oromanovna_diploma/allure/).

## Запуск автотестов

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

## Интеграция с Jenkins
- для запуска тестов на сервере настроена job'a в Jenkins.
<img src="resources/picture/jenkins.png" alt="jenkins_job"/>

## Интеграция с Allure
- после прохождения тестов будет собран отчёт на основе генератора Allure;
<img src="resources/picture/dash_local_allure.png" alt="dash_local_allure"/>
- к api тестам приложены logs, cUrl;
<img src="resources/picture/logs_curl.png" alt="logs_curl"/>
- к UI тестам приложены video, html, logs, screenshot;
<img src="resources/picture/logs_ui.png" alt="logs_ui"/>

## Интеграция с Allure TestOps
- результаты прохождения тестов, а также сами тест-кейсы будут отправлены в TestOps Allure;
<img src="resources/picture/test_ops_test_cases.png" alt="test_ops_test_cases"/>
- на основе результатов будет сгенерирован дашборд
<img src="resources/picture/test_ops_dash.png" alt="test_ops_dash"/>

## Интеграция с Jira
- в задачу регресса добавлены пройденные тест-кейсы
- а также запущенный лаунч
<img src="resources/picture/jira.png" alt="jira"/>

## Нотификация в Telegram
- после прохождения тестов результаты будут отправлены в Telegram;  
<img src="resources/picture/telegram_not.png" width="500">

## Пример прохождения UI-теста
<img src="resources/picture/1e66982f003b2056cd1399b13bfd11c9.gif">
