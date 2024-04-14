from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
import allure




class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def open_page(self, subdir=''):
        url = Constants.MAIN_PAGE_URL+subdir
        return self.driver.get(url)

    @allure.step('Проверка текущего url')
    def check_page(self, subdir=''):
        combined_url = Constants.MAIN_PAGE_URL + subdir
        return self.driver.current_url == combined_url

    @allure.step('Ожидание загрузки заголовка страницы')
    def wait_for_load(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Поиск элемента по локатору')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    @allure.step('Ввод текста в элемент')
    def send_keys_to_element(self, locator, keys=None):

        self.find_element_located(locator).send_keys(keys)

    @allure.step('Клик по элементу')
    def click_element(self, locator, time=10):
        element = self.find_element_located(locator, time)
        return element.click()

    @allure.step('Получение текста, который находится по локатору')
    def get_text_by_locator(self, locator):
        return self.find_element_located(locator).text

    @allure.step('Получение элемента по локатору')
    def get_element_by_locator(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Перетаскивание элемента на элемент')
    def do_drag_n_drop(self, source, target):
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step('Ожидание исчезновения элемента')
    def wait_until_not_present(self, locator, time=10):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step('Проверка видимости всплывающего окна')
    def check_pop_open(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

