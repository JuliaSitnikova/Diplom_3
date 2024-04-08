import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from locators.authoriz_locators import Authorization


class PageEntrance(BasePage):

    @allure.step('Ожидание загрузки заголовка страницы входа')
    def wait_for_entrance_header_load(self):
        return self.wait_for_load(Authorization.ENTRANCE_HEADER)

    @allure.step('Клик на ссылку восстановления пароля')
    def click_recovery_password(self):
        return self.click_element(Authorization.BUTTON_RESTORE_PASSWORD)

    @allure.step('Ввод в поле email')
    def enter_email(self, email):
        self.send_keys_to_element(locator=Authorization.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        self.send_keys_to_element(locator=Authorization.PASSWORD_INPUT_FIELD, keys=password)

    @allure.step('Клик на кнопку Войти')
    def click_button_enter(self):
        return self.click_element(Authorization.BUTTON_ENTER)

    @allure.step('Клик на конструктор')
    def click_constructor(self):
        return self.click_element(MainLocators.MENU_CONSTRUCTOR)

    @allure.step('Заполнение полей email/пароль, клик на вход')
    def fill_email_and_password_and_enter(self, email='', password=''):
        self.wait_for_entrance_header_load()
        self.enter_email(email)
        self.enter_password(password)
        self.click_button_enter()
        self.check_page()