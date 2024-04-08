import allure
from pages.recovery_password_page import RecoveryPasswordPage
from locators.password_locators import PasswordLocators




class ResetPasswordPage(RecoveryPasswordPage):
    @allure.step('Клик на кнопку Показать пароль')
    def click_show_password(self):
        self.click_element(PasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверка поля ввода пароля')
    def check_show_password(self):
        return self.find_element_located(PasswordLocators.ACTIVE_PASSWORD_INPUT_FIELD)