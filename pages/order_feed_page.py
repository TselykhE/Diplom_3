import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Открыть модальное окно с деталями заказа')
    def open_modal_window_order_details(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_FEED_LIST)

    @allure.step('Получить номер заказа в работе')
    def order_number_in_work(self):
        return self.text_element(OrderFeedPageLocators.ORDER_LIST_READY)

    @allure.step("Получить класс модального окна с деталями заказа")
    def get_class_detail_modal_window(self):
        detail_modal_window = self.class_element(OrderFeedPageLocators.ORDER_DETAIL_MODAL_WINDOW)
        return detail_modal_window

    @allure.step('Получить список заказов')
    def get_number_list_feed(self):
        numbers = self.find_elements_and_wait(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
        order_list = [number.text for number in numbers]
        return order_list

    @allure.step('Получить список заказов за всё время')
    def get_number_orders_all_time(self):
        return self.text_element(OrderFeedPageLocators.ALL_ORDERS)

    @allure.step('Получить список заказов за сегодня')
    def get_number_orders_today(self):
        return self.text_element(OrderFeedPageLocators.ALL_ORDERS_TODAY)
