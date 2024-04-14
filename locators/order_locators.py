from selenium.webdriver.common.by import By

class OrderLocators:
 ORDER_LIST_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")
 FIRST_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                          "'text_type_digits')]")
 ORDER_DETAILS_POPUP = (By.XPATH, ".//div[contains(@class,'Modal_orderBox')]")
 ORDER_DETAILS_POPUP_ORDER_ID_XPATH = (By.XPATH, ".//div[contains(@class,'Modal_orderBox')]/p")
 TOTAL_COUNT_XPATH = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
 TODAY_COUNT_XPATH = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
 FIRST_ORDERS_HISTORY_ORDER = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]/a/div/p[contains(@class, "
                                         "'text_type_digits')]")
 ORDER_LOCATOR_A = "//p[contains(text(), '"
 ORDER_LOCATOR_B = "')]"
 ORDER_LOCATOR_C = "///li[text()='{}']"
 ORDER_LOCATOR_D = "']"
 ORDER_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady_')]")