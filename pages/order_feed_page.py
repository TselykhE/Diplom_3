from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    def open_modal_window_order_details(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_FEED_LIST)

    def order_number_in_work(self):
        return self.text_element(OrderFeedPageLocators.ORDER_LIST_READY)

    def get_class_detail_modal_window(self):
        detail_modal_window = self.class_element(OrderFeedPageLocators.ORDER_DETAIL_MODAL_WINDOW)
        return detail_modal_window

    def get_number_list_feed(self):
        numbers = self.find_elements_and_wait(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
        order_list = [number.text for number in numbers]
        return order_list

    def get_number_orders_all_time(self):
        return self.text_element(OrderFeedPageLocators.ALL_ORDERS)

    def get_number_orders_today(self):
        return self.text_element(OrderFeedPageLocators.ALL_ORDERS_TODAY)
