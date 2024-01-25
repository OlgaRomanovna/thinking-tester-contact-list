import allure
from selene import browser, have
from thinking_tester_contact_list.data import data


class RegisterPage:
    @allure.step('Кликаем по кнопке регистрации')
    def open(self):
        browser.element('#signup').click()

    @allure.step('Заполняем форму регистрации')
    def fill_form(self):
        browser.element('#firstName').type(data.first_name_for_register)
        browser.element('#lastName').type(data.last_name_for_register)
        browser.element('#email').type(data.email_for_register_for_ui)
        browser.element('#password').type(data.password)

    @allure.step('Подтверждаем данные')
    def submit(self):
        browser.element('#submit').click()

    @allure.step('Нажимаем кнопку Cancel')
    def cancel(self):
        browser.element('#cancel').click()

    @allure.step('Проверяем результат успешной регистрации')
    def check_after_positive_register(self, header: str):
        browser.element('body > div > header > h1').should(have.text(header))

    @allure.step('Проверяем результат, когда форма регистрации не заполнена')
    def check_after_negative_register(self, name_error: str):
        browser.element('#error').should(have.text(name_error))
