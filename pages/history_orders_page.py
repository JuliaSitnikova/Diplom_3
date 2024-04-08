from pages.base_page import BasePage
import allure
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators


class HistoryOrdersPage(BasePage):
    @allure.step('Ожидание загрузки первого заказа в ленте заказов')
    def wait_order_load(self):
        self.wait_for_load(OrderLocators.FIRST_ORDER)

    @allure.step('Проверка наличие id заказа в истории заказов')
    def check_order_id_in_history_orders(self, order_id):
        or_a = OrderLocators.ORDER_LOCATOR_A
        or_b = OrderLocators.ORDER_LOCATOR_B
        locator = f"{or_a}+{order_id}+{or_b}"
        self.check_pop_open(locator)

    @allure.step('Клик на ленту заказов')
    def click_list_orders(self):
        self.click_element(MainLocators.ORDER_LINE)