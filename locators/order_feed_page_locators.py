from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    ORDER_FEED_LIST = By.XPATH, '(//ul[@class="OrderFeed_list__OLh59"])[1]'
    ORDER_DETAIL_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal__container__Wo2l_'
    ORDER_NUMBER_IN_FEED = By.XPATH, '//p[@class="text text_type_digits-default"]'
    ALL_ORDERS = By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ALL_ORDERS_TODAY = By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    ORDER_LIST_READY = By.XPATH, './/*[contains(@class, "orderListReady")]//*[contains(@class, "digits-default")]'
