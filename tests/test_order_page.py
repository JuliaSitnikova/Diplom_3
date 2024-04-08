import allure
from constants import Constants
from pages.list_orders_page import ListOrdersPage
from pages.main_page import MainPage
from pages.page_entrance import PageEntrance
from pages.profile_page import ProfilePage
from pages.history_orders_page import HistoryOrdersPage



class TestOrderList:
    @allure.title('Проверить, что при клике на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_main_page_header_load()
        main_page.click_orders_list_button()
        list_orders = ListOrdersPage(driver)
        list_orders.wait_orders_list_load()
        order_id = list_orders.get_first_id_order()
        list_orders.click_order_to_id(order_id)
        new_id = list_orders.get_id_order_from_modal()
        assert list_orders.check_details_order_modal_open() and order_id == new_id

    @allure.title('Проверить, что заказы пользователя из истории заказов есть в ленте заказов')
    def test_new_order_availability_in_orders_list(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.make_order()
        order_id = main_page.get_order_id()
        main_page.click_popup_close()
        main_page.click_lk_button()
        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_load()
        profile_page.click_history_orders_section_name()
        history_orders = HistoryOrdersPage(driver)
        history_orders.wait_order_load()
        history_orders.click_list_orders()
        list_orders = ListOrdersPage(driver)
        list_orders.wait_orders_list_load()
        assert list_orders.check_id_order_in_orders_list(order_id)

    @allure.title('Проверка, что заказы из истории заказов отображаются на странице ленты заказов')
    def test_new_orders_added_total_today_orders_count(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.click_orders_list_button()
        list_orders = ListOrdersPage(driver)
        list_orders.wait_orders_list_load()
        alltime_count = list_orders.get_alltime_count()
        today_count = list_orders.get_today_count()
        orders_list = ListOrdersPage(driver)
        orders_list.click_constructor()
        main_page.make_order()
        main_page.click_popup_close()
        main_page.click_orders_list_button()
        orders_list.wait_orders_list_load()
        new_alltime_count = orders_list.get_alltime_count()
        new_today_count = orders_list.get_today_count()
        assert new_alltime_count > alltime_count and new_today_count > today_count

    @allure.title('Проверить, что после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_availability_in_work_orders(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.make_order()
        order_id = main_page.get_order_id()
        main_page.click_popup_close()
        main_page.click_orders_list_button()
        list_orders = ListOrdersPage(driver)
        list_orders.wait_orders_list_load()
        assert list_orders.check_id_order_at_work_orders(order_id)