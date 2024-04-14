import allure
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage



class ProfilePage(BasePage):

    @allure.step('Клик на заголовок в Истории заказов')
    def click_history_orders_section_name(self):
        return self.click_element(ProfileLocators.ORDERS_HISTORY_AREA)

    @allure.step('Ожидание загрузки заголовка Профиля')
    def wait_for_profile_load(self):
        return self.wait_for_load(ProfileLocators.PROFILE_AREA)

    @allure.step('Клик на Выход')
    def click_exit_button(self):
        return self.click_element(ProfileLocators.BUTTON_EXIT_ACCOUNT)