import allure
from data import *
from pages.password_recovery_page import PasswordRecoveryPage
from pages.basic_func_page import BasicFuncPage
from conftests import*


class TestBasicFuncPage:

    @allure.title('Переход по клику на «Конструктор»')
    def test_constructor_button(self, driver):
        basic = BasicFuncPage(driver)
        basic.open_url()
        basic.click_on_personal_account_button()
        basic.click_on_constructor_button()
        current_url = basic.get_current_url()
        assert current_url == Urls.BASE_URL

    @allure.title('Переход по клику на «Лента заказов»')
    def test_order_feed_button(self, driver):
        basic = BasicFuncPage(driver)
        basic.open_url()
        basic.click_on_personal_account_button()
        basic.click_on_order_feed_button()
        current_url = basic.get_current_url()
        assert current_url == Urls.ORDER_FEED_URL

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_modal_window_ingredient(self, driver):
        basic = BasicFuncPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_ingredient_button()
        current_url = basic.get_current_url()
        assert Urls.INGREDIENT_URL in current_url

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_modal_window_ingredient(self, driver):
        basic = BasicFuncPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_ingredient_button()
        basic.close_modal_window()
        assert basic.get_class_close_modal_window() == ModalWindow.MODAL_WINDOW_CLOSE

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_change_ingredient_counter(self, driver):
        basic = BasicFuncPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.add_ingredient()
        assert basic.number_count() == UserData.NUMBER_COUNT

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_get_order_with_log_in_user(self, driver):
        basic = BasicFuncPage(driver)
        password = PasswordRecoveryPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        password.add_auth_field_click()
        basic.add_ingredient()
        basic.wait_overlaying_window_disappear()
        basic.click_on_order_button()
        assert basic.find_modal_window()
