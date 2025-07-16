from data import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from locators.basic_func_page_locators import BasicFuncPageLocators


class BasicFuncPage(BasePage):

    def open_url(self):
        self.go_to_url(Urls.BASE_URL)

    def wait_overlaying_window_disappear(self):
        self.wait_for_invisibility_of_element(BasePageLocators.PROBLEM_MODAL)

    def find_modal_window(self):
        if self.find_element_and_wait(BasicFuncPageLocators.ORDER_MODAL_WINDOW):
            return True
        else:
            return False

    def get_class_close_modal_window(self):
        close_modal_window = self.class_element(BasicFuncPageLocators.INGREDIENT_CLOSE_MODAL_WINDOW)
        return close_modal_window

    def click_on_log_in_button(self):
        self.click_on_element(BasicFuncPageLocators.LOG_IN_ACCOUNT_MAIN)

    def click_on_personal_account_button(self):
        self.click_on_element(BasicFuncPageLocators.PERSONAL_ACCOUNT)

    def click_on_order_feed_button(self):
        self.click_on_element(BasicFuncPageLocators.ORDER_FEED_BUTTON)

    def click_on_constructor_button(self):
        self.click_on_element(BasicFuncPageLocators.CONSTRUCTOR_BUTTON)

    def click_on_ingredient_button(self):
        self.click_on_element(BasicFuncPageLocators.INGREDIENT_BUTTON)

    def modal_window(self):
        return self.find_element_and_wait(BasicFuncPageLocators.MODAL_WINDOW).text()

    def close_modal_window(self):
        self.find_element_and_wait(BasicFuncPageLocators.CLOSE_MODAL_WINDOW_BUTTON)
        self.click_on_element(BasicFuncPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    def add_ingredient(self):
        element_from = self.find_element_and_wait(BasicFuncPageLocators.INGREDIENT_BUTTON)
        element_to = self.find_element_and_wait(BasicFuncPageLocators.BURGER_INGREDIENT)
        self.drag_and_drop_element(element_from, element_to)

    def click_on_order_button(self):
        self.click_on_element(BasicFuncPageLocators.ORDER_BUTTON)

    def number_count(self):
        return self.text_element(BasicFuncPageLocators.INGREDIENT_COUNTER)

    def new_order_number(self):
        self.wait_for_page_load()
        return f'0{self.text_element(BasicFuncPageLocators.ORDER_NUMBER_FROM_MODAL)}'
