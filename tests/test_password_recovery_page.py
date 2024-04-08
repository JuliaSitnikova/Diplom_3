import allure
from constants import Constants
from pages.page_entrance import PageEntrance
from pages.recovery_password_page import RecoveryPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке восстановить пароль')
    def test_password_recovery_gives_recovery_page(self, driver):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(subdir=Constants.ENTRANCE_PAGE)
        page_entrance.wait_for_entrance_header_load()
        page_entrance.click_recovery_password()
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.wait_for_recovery_page_load()
        assert recovery_password_page.check_page(subdir=Constants.RECOVER_PASSWORD)

    @allure.title('По кнопке Восстановить пароль переходим на страницу восстановления пароля')
    def test_password_reset_valid_email(self, driver, make_user, create_user_payload):
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_page(subdir=Constants.RECOVER_PASSWORD)
        recovery_password_page.wait_for_recovery_page_load()
        email = payload["email"]
        recovery_password_page.enter_email(email)
        recovery_password_page.click_recover_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_recovery_page_load()
        assert reset_password_page.check_page(subdir=Constants.RECOVER_PASSWORD)

    @allure.title('Проверить, что кнопка Показать пароль делает активным поле для ввода пароля')
    def test_password_reset_gets_highlighted(self, driver, make_user, create_user_payload):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_page(Constants.RECOVER_PASSWORD)
        recovery_password_page.wait_for_recovery_page_load()
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        email = payload["email"]
        recovery_password_page.enter_email(email)
        recovery_password_page.click_recover_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_recovery_page_load()
        reset_password_page.check_page(subdir=Constants.RESET_PASSWORD)
        reset_password_page.click_show_password()
        assert reset_password_page.check_show_password()