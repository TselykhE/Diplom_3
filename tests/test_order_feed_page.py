import re

import allure
from data import ModalWindow
from pages.base_page import BasePage
from pages.basic_func_page import BasicFuncPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from conftests import*

class TestOrderFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_modal_window_order_details(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        order = OrderFeedPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_feed_button()
        order.open_modal_window_order_details()
        assert order.get_class_detail_modal_window() == ModalWindow.DETAIL_MODAL_WINDOW

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_displaying_history_in_order_feed(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        order = OrderFeedPage(driver)
        personal = PersonalAccountPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.wait_overlaying_window_disappear()
        basic.click_on_personal_account_button()
        personal.click_on_history_button()
        number_list = order.get_number_list_feed()
        assert personal.order_number_history() in number_list

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all_orders(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        order = OrderFeedPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_feed_button()
        amount = order.get_number_orders_all_time()
        basic.click_on_constructor_button()
        basic.add_ingredient()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_button()
        basic.wait_overlaying_window_disappear()
        basic.close_modal_window()
        basic.click_on_order_feed_button()
        assert int(amount) + 1

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_today_orders(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        order = OrderFeedPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_feed_button()
        amount = order.get_number_orders_today()
        basic.click_on_constructor_button()
        basic.add_ingredient()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_button()
        basic.wait_overlaying_window_disappear()
        basic.close_modal_window()
        basic.click_on_order_feed_button()
        assert int(amount) + 1

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_counter_order_in_work(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        order = OrderFeedPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.add_ingredient()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_button()
        basic.wait_overlaying_window_disappear()
        new_order = basic.new_order_number()
        basic.wait_overlaying_window_disappear()
        basic.close_modal_window()
        basic.click_on_order_feed_button()
        order_in_work = order.order_number_in_work()
        assert new_order.isdigit() == order_in_work.isdigit()
