from pages.base_page import BasePage
from locators.main_locators import MainLocators
import allure


class MainPage(BasePage):

    @allure.step('Ожидание загрузки заголовка главной страницы')
    def wait_main_page_header_load(self):
        self.wait_for_load(MainLocators.MAIN_PAGE_HEADER)

    @allure.step('Клик на Личный кабинет')
    def click_lk_button(self):
        return self.click_element(MainLocators.PRIVATE_AREA)

    @allure.step('Проверка, что у незалогиненного пользователя есть кнопка Войти')
    def check_enter_button(self):
        return self.find_element_located(MainLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step('Проверка, что у незалогиненного пользователя есть кнопка Войти Оформить заказ')
    def check_make_order_button(self):
        return self.find_element_located(MainLocators.BUTTON_MAKE_ORDER)

    @allure.step('Клик по кнопке Лента Заказов')
    def click_orders_list_button(self):
        return self.click_element(MainLocators.ORDER_LINE)

    @allure.step('Клик на первый ингредиент')
    def click_first_ingredient(self):
        return self.click_element(MainLocators.FIRST_INGREDIENT)

    @allure.step('Проверка наличия всплывающего окна')
    def check_popup_open(self):
        return self.check_pop_open(MainLocators.INGREDIENT_POPUP_XPATH)

    @allure.step('Ожидание загрузки заголовка всплывающего окна')
    def wait_popup_header_load(self):
        self.wait_for_load(MainLocators.INGREDIENT_POPUP_HEADER)

    @allure.step('Клик на крестик на всплывающем окне')
    def click_popup_close(self):
        self.wait_until_not_present(MainLocators.OVERLAY_POPUP)
        self.wait_for_load(MainLocators.CLOSE_POPUP).click()

    @allure.step('Получение значения счетчика ингредиента')
    def get_first_ingredient_value(self):
        return int(self.get_element_by_locator(MainLocators.FIRST_INGREDIENT_COUNTER_XPATH).text)

    @allure.step('Перетаскивание первого ингредиента в корзину')
    def drag_n_drop_first_ingredient_in_basket(self):
        return self.do_drag_n_drop(source=MainLocators.FIRST_INGREDIENT, target=MainLocators.BASKET)

    @allure.step('Клик на Оформить заказ')
    def click_make_order(self):
        self.click_element(MainLocators.BUTTON_MAKE_ORDER)

    @allure.step('Получение ID заказа')
    def get_order_id(self):

        self.wait_until_not_present(MainLocators.TEMPORARY_ORDER_POPUP_HEADER)
        return self.get_text_by_locator(MainLocators.ORDER_ID_XPATH)

    @allure.step('Создание заказа перетаскиванием')
    def make_order(self):
        self.drag_n_drop_first_ingredient_in_basket()
        self.click_make_order()