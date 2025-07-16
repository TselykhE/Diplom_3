import allure
from data import Urls
from pages.basic_func_page import BasicFuncPage
from pages.password_recovery_page import PasswordRecoveryPage
from conftests import*

class TestPasswordRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_recovery_password_button(self, driver):
        basic = BasicFuncPage(driver)
        password = PasswordRecoveryPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        password.click_on_recovery_password_button()
        current_url = password.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD_URL


    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_add_email_and_click_on_recovery_password_button(self, driver):
        basic = BasicFuncPage(driver)
        password = PasswordRecoveryPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        password.click_on_recovery_password_button()
        password.add_email()
        password.click_on_recovery_button()
        password.wait_load_password_recovery_page()
        current_url = password.get_current_url()
        assert current_url == Urls.RESET_PASSWORD_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_show_hidden_button(self, driver):
        basic = BasicFuncPage(driver)
        password = PasswordRecoveryPage(driver)
        basic.open_url()
        basic.wait_overlaying_window_disappear()
        basic.click_on_log_in_button()
        password.click_on_recovery_password_button()
        password.add_email()
        password.click_on_recovery_button()
        basic.wait_overlaying_window_disappear()
        password.click_on_show_hidden_button()
        assert password.click_on_show_hidden_button()
