import allure
from selene import have, browser
from thinking_tester_contact_list.data import data


class AddContactPage:

    @allure.step('Кликаем по кнопке "Add a New Contact"')
    def open(self):
        browser.element('#add-contact').click()

    @allure.step('Заполняем форму контакта')
    def fill_form(self):
        browser.element('#firstName').type(data.first_name)
        browser.element('#lastName').type(data.last_name)
        browser.element('#birthdate').type(data.birthdate)
        browser.element('#email').type(data.email)
        browser.element('#phone').type(data.phone)
        browser.element('#street1').type(data.street1)
        browser.element('#street2').type(data.street2)
        browser.element('#city').type(data.city)
        browser.element('#stateProvince').type(data.state_province)
        browser.element('#postalCode').type(data.postal_code)
        browser.element('#country').type(data.country)

    @allure.step('Подтверждаем введённые данные')
    def submit(self):
        browser.element('#submit').click()

    @allure.step('Проверяем результат в общем списке контактов')
    def check_result(self):
        browser.element('#myTable > tr:nth-child(3) > td:nth-child(2)').should(have.text(
            data.first_name))
        browser.element('#myTable > tr:nth-child(3) > td:nth-child(3)').should(have.text(data.birthdate))
        browser.element('#myTable > tr:nth-child(3) > td:nth-child(4)').should(have.text(data.email))
        browser.element('#myTable > tr:nth-child(3) > td:nth-child(6)').should(have.text(
            f'{data.street1} {data.street2}'))
        browser.element('#myTable > tr:nth-child(3) > td:nth-child(7)').should(have.text(
            f'{data.city} {data.state_province} {data.postal_code}'
        ))
        browser.element('#myTable > tr > td:nth-child(8)').should(have.text(data.country))


add_contact_page = AddContactPage()
