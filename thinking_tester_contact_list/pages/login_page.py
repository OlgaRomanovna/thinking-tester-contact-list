import allure
from selene import browser, have
from thinking_tester_contact_list.data import data


class LoginPage:

    @allure.step('Отрываем страницу страницу логина')
    def open(self):
        browser.open('/login')

    @allure.step('Заполняем форму логина')
    def fill_form(self):
        browser.element('#email').type(data.email)
        browser.element('#password').type(data.password)

    @allure.step('Заполняем форму логина')
    def fill_form_incorrect(self):
        browser.element('#email').type('incorrect@mail.ru')
        browser.element('#password').type('incorrect_password')

    @allure.step('Подтверждаем введённые данные')
    def submit(self):
        browser.element('#submit').click()

    @allure.step('Проверяем результат после авторизации')
    def check_result_after_login(self, header: str, sub_header: str):
        browser.element('body > div > header > h1').should(have.text(header))
        browser.element('body > div > p:nth-child(2)').should(have.text(sub_header))
        browser.element('#logout').should(have.text('Logout'))

    @allure.step('Проверяем результат после введения некорректных авторизационных данных')
    def check_result_after_incorrect_login_data(self, name_error: str):
        browser.element('#error').should(have.text(name_error))

    @allure.step('Проверяем ссылку на странице')
    def check_link(self):
        browser.element('body > div:nth-child(3) > a').click()


