import allure
from selene import browser, have


class LogoutPage:

    @allure.step('Выполняем деавторизацию')
    def log_out(self):
        browser.element('#logout').click()

    @allure.step('Проверяем результат после деавторизации')
    def check_result_after_log_out(self, header: str, sub_header: str, href: str):
        browser.element('body > h1').should(have.text(header))
        browser.element('body > div:nth-child(2)').should(have.text(sub_header))
        browser.element('body > div:nth-child(3) > a').should(have.text(href))
