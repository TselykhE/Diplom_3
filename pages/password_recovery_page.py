import allure

from data import UserData
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from locators.base_page_locators import BasePageLocators


class PasswordRecoveryPage(BasePage):

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_recovery_password_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_recovery_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Ожидание загрузки страницы восстановления пароля')
    def wait_load_password_recovery_page(self):
        self.wait_for_page_load()
        self.find_element_and_wait(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_INPUT)

    @allure.step('Клик по кнопке "Показать/Скрыть пароль"')
    def click_on_show_hidden_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.SHOW_HIDDEN_BUTTON)
        return PasswordRecoveryPageLocators.ACTIV_FIELD_PASSWORD

    @allure.step('Заполнить поле "Email"')
    def add_email(self):
        self.add_text(BasePageLocators.EMAIL_INPUT, UserData.RECOVERY_EMAIL)
