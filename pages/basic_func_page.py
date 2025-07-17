import allure

from data import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from locators.basic_func_page_locators import BasicFuncPageLocators


class BasicFuncPage(BasePage):

    @allure.step('Открыть страницу по урлу')
    def open_url(self):
        self.go_to_url(Urls.BASE_URL)

    @allure.step('Ожидание скрытия перекрывающего окна')
    def wait_overlaying_window_disappear(self):
        self.wait_for_invisibility_of_element(BasePageLocators.PROBLEM_MODAL)

    @allure.step('Найти модальное окно')
    def find_modal_window(self):
        if self.find_element_and_wait(BasicFuncPageLocators.ORDER_MODAL_WINDOW):
            return True
        else:
            return False

    @allure.step('Получить класс модального окна Детали ингредиента')
    def get_class_close_modal_window(self):
        close_modal_window = self.class_element(BasicFuncPageLocators.INGREDIENT_CLOSE_MODAL_WINDOW)
        return close_modal_window

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_log_in_button(self):
        self.click_on_element(BasicFuncPageLocators.LOG_IN_ACCOUNT_MAIN)

    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_on_personal_account_button(self):
        self.click_on_element(BasicFuncPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_on_order_feed_button(self):
        self.click_on_element(BasicFuncPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(BasicFuncPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient_button(self):
        self.click_on_element(BasicFuncPageLocators.INGREDIENT_BUTTON)

    @allure.step('Получить модальное окно Детали ингредиента')
    def modal_window(self):
        return self.find_element_and_wait(BasicFuncPageLocators.MODAL_WINDOW).text()

    @allure.step('Закрыть модальное окно Детали ингредиента')
    def close_modal_window(self):
        self.find_element_and_wait(BasicFuncPageLocators.CLOSE_MODAL_WINDOW_BUTTON)
        self.click_on_element(BasicFuncPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient(self):
        element_from = self.find_element_and_wait(BasicFuncPageLocators.INGREDIENT_BUTTON)
        element_to = self.find_element_and_wait(BasicFuncPageLocators.BURGER_INGREDIENT)
        self.drag_and_drop_element(element_from, element_to)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_element(BasicFuncPageLocators.ORDER_BUTTON)

    @allure.step('Получить значение счётчика ингредиента')
    def number_count(self):
        return self.text_element(BasicFuncPageLocators.INGREDIENT_COUNTER)

    @allure.step('Получить номер оформленного заказа')
    def new_order_number(self):
        self.wait_for_page_load()
        return f'0{self.text_element(BasicFuncPageLocators.ORDER_NUMBER_FROM_MODAL)}'
