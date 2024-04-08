import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators

class ListOrdersPage(BasePage):

    @allure.step('Ожидание загрузки заголовка страницы ленты заказов')
    def wait_orders_list_load(self):
        self.wait_for_load(OrderLocators.ORDER_LIST_HEADER)

    @allure.step('Получение id первого заказа')
    def get_first_id_order(self):
        return self.get_text_by_locator(OrderLocators.FIRST_ORDER)

    @allure.step('Клик на заказ Ленты Заказов по номеру')
    def click_order_to_id(self, order_id):
        or_a = OrderLocators.ORDER_LOCATOR_A
        or_b = OrderLocators.ORDER_LOCATOR_B
        locator = f"{or_a}{order_id}{or_b}"
        selector = (By.XPATH, locator)
        self.click_element(selector)

    @allure.step('Проверка видимости модального окна')
    def check_details_order_modal_open(self):
        return self.check_pop_open(OrderLocators.ORDER_DETAILS_POPUP)

    @allure.step('Получение id заказа из заголовка модального окна')
    def get_id_order_from_modal(self):
        return self.get_text_by_locator(OrderLocators.ORDER_DETAILS_POPUP_ORDER_ID_XPATH)

    @allure.step('Проверка наличия id заказа в ленте заказов')
    def check_id_order_in_orders_list(self, order_id):
        or_a = OrderLocators.ORDER_LOCATOR_A
        or_b = OrderLocators.ORDER_LOCATOR_B
        locator = (By.XPATH, f"{or_a}{order_id}{or_b}")
        print(order_id)
        return self.check_element_exists_with_wait(locator)

    @allure.step('Клик на Конструктор')
    def click_constructor(self):
        return self.click_element(MainLocators.MENU_CONSTRUCTOR)

    @allure.step('Получение значения счетчика Выполнено за все время')
    def get_alltime_count(self):
        return self.get_text_by_locator(OrderLocators.TOTAL_COUNT_XPATH)

    @allure.step('Получение значения счетчика Выполнено за сегодня')
    def get_today_count(self):
        return self.get_text_by_locator(OrderLocators.TODAY_COUNT_XPATH)

    @allure.step('Проверка наличия id заказа в работе')
    def check_id_order_at_work_orders(self, order_id):
        or_c = OrderLocators.ORDER_LOCATOR_C
        or_d = OrderLocators.ORDER_LOCATOR_D
        locator = (By.XPATH, f"{or_c}{order_id}{or_d}")
        print(order_id)
        elem = self.find_element_located(OrderLocators.ORDER_FEED)
        print(elem)
        print(elem.text)
        return self.check_pop_open(locator)