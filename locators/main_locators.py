from selenium.webdriver.common.by import By
class MainLocators:
    MAIN_PAGE_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок на главной странице
    PRIVATE_AREA = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Главная страница, кнопка перехода в Личный кабинет
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка на главной странице, доступная
    # только после входа пользователя в аккаунт
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт на гл. странице
    MENU_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка Конструктор на хедере главной страницы
    ORDER_LINE = (By.XPATH, "//p[text() = 'Лента Заказов']")  # Кнопка Лента Заказов на хедере главной страницы
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    FIRST_INGREDIENT_COUNTER_XPATH = (By.XPATH, "//p[contains(@class, 'counter_counter')][1]")
    INGREDIENT_POPUP_XPATH = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened_')]")
    CLOSE_POPUP = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    OVERLAY_POPUP = (By.XPATH, "//img[contains(@class, 'Modal_modal__loading')]")
    INGREDIENT_POPUP_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")  # Общий локатор для корзины
    TEMPORARY_ORDER_POPUP_HEADER = (By.XPATH, "//h2[text()='9999']")
    ORDER_ID_XPATH = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")