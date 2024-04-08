import allure
from constants import Constants
from pages.main_page import MainPage
from pages.page_entrance import PageEntrance
from pages.profile_page import ProfilePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCabinetUser:
    @allure.title('Переход в личный кабинет пользователя по клику на личный кабинет')
    def test_main_page_to_cabinet_user(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)

        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.wait_for_entrance_header_load()
        page_entrance.enter_email(payload["email"])
        page_entrance.enter_password(payload["password"])
        page_entrance.click_button_enter()
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.click_lk_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_load()
        assert profile_page.check_page(Constants.PROFILE_PAGE)

    @allure.title('Проверка перехода из личного кабинета в историю заказов')
    def test_order_list_from_cabinet_user(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.click_lk_button()
        main_page.check_page(Constants.PROFILE_PAGE)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_load()
        profile_page.check_page(Constants.PROFILE_PAGE)
        profile_page.click_history_orders_section_name()
        assert page_entrance.check_page(Constants.ORDER_HISTORY)

    @allure.title('Проверка выхода из аккаунта')
    def test_account_logout(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.click_lk_button()
        main_page.check_page(Constants.PROFILE_PAGE)
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_load()
        profile_page.check_page(Constants.PROFILE_PAGE)
        profile_page.click_exit_button()
        page_entrance.check_page(Constants.ENTRANCE_PAGE)
        page_entrance.wait_for_entrance_header_load()
        page_entrance.click_constructor()
        page_entrance.check_page()
        main_page.wait_main_page_header_load()
        assert main_page.check_enter_button()