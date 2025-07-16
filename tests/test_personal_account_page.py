import allure
from data import Urls
from pages.base_page import BasePage
from pages.basic_func_page import BasicFuncPage
from pages.personal_account_page import PersonalAccountPage
from conftests import*

class TestPersonalAccountPage:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_click_button_personal_account(self, driver):
        basic = BasicFuncPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        current_url = basic.get_current_url()
        assert current_url == Urls.LOGIN_URL

    @allure.title('Переход в раздел «История заказов»')
    def test_history_order(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        personal = PersonalAccountPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.wait_overlaying_window_disappear()
        basic.click_on_personal_account_button()
        personal.click_on_history_button()
        basic.wait_for_page_load()
        current_url = personal.get_current_url()
        assert current_url == Urls.ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_exit_button(self, driver):
        basic = BasicFuncPage(driver)
        base = BasePage(driver)
        personal = PersonalAccountPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        base.add_auth_field_click()
        basic.wait_overlaying_window_disappear()
        basic.click_on_personal_account_button()
        personal.click_on_exit_button()
        base.find_log_in_button()
        current_url = personal.get_current_url()
        assert current_url == Urls.LOGIN_URL
