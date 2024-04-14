import allure
from pages.base_page import BasePage
from locators.password_locators import PasswordLocators


class RecoveryPasswordPage(BasePage):

    @allure.step('Ожидание загрузки заголовка страницы Восстановления пароля')
    def wait_for_recovery_page_load(self):
        self.wait_for_load(PasswordLocators.HEADER_RESTORE_PASSWORD)

    @allure.step('Ввод значения имейл')
    def enter_email(self, email):
        self.send_keys_to_element(locator=PasswordLocators.EMAIL_INPUT_FIELD, keys=email)

    @allure.step('Клик на кнопку восстановления пароля')
    def click_recover_button(self):
        self.click_element(PasswordLocators.BUTTON_RESTORE_PASSWORD)