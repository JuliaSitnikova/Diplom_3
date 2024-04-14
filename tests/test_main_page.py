import allure
from constants import Constants
from pages.list_orders_page import ListOrdersPage
from pages.main_page import MainPage
from pages.page_entrance import PageEntrance



class TestMainFunction:

    @allure.title('Проверка перехода из личного кабинета в Конструктор')
    def test_go_over_in_constructor(self, driver):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        page_entrance.wait_for_entrance_header_load()
        page_entrance.click_constructor()
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        assert main_page.check_page()

    @allure.title('Проверка перехода с основной страницы в Ленту Заказов')
    def test_go_over_in_orders_line(self, driver):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        page_entrance.click_constructor()
        page_entrance.check_page()
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.click_orders_list_button()
        list_orders = ListOrdersPage(driver)
        assert list_orders.check_page(Constants.ORDER_LINE)

    @allure.title('Проверить, что при клике на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient_opens_popup_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_main_page_header_load()
        main_page.click_first_ingredient()
        main_page.wait_popup_header_load()
        assert main_page.check_popup_open()

    @allure.title('Проверка закрытия всплывающего окна с помощью крестика')
    def test_click_with_x_close_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_main_page_header_load()
        main_page.click_first_ingredient()
        main_page.wait_popup_header_load()
        main_page.click_popup_close()
        assert not main_page.check_popup_open()

    @allure.title('Проверка, что при добавлении ингредиента в заказ увеличивается счетчик этого ингредиента')
    def test_drag_and_drop_ingredient_in_basket_plus_count(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.wait_main_page_header_load()
        initial_value = main_page.get_first_ingredient_value()
        main_page.drag_n_drop_first_ingredient_in_basket()
        updated_value = main_page.get_first_ingredient_value()
        assert initial_value < updated_value

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_login_user_make_order(self, driver, make_user, create_user_payload):
        page_entrance = PageEntrance(driver)
        page_entrance.open_page(Constants.ENTRANCE_PAGE)
        payload = create_user_payload(name='rand', password='rand', email='rand')
        user = make_user(data=payload)
        page_entrance.fill_email_and_password_and_enter(email=payload["email"], password=payload["password"])
        main_page = MainPage(driver)
        main_page.wait_main_page_header_load()
        main_page.check_make_order_button()
        main_page.drag_n_drop_first_ingredient_in_basket()
        main_page.click_make_order()
        assert main_page.check_popup_open()

