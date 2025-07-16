from data import UserData
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from locators.base_page_locators import BasePageLocators


class PasswordRecoveryPage(BasePage):

    def click_on_recovery_password_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    def click_on_recovery_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    def wait_load_password_recovery_page(self):
        self.wait_for_page_load()
        self.find_element_and_wait(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_INPUT)

    def click_on_show_hidden_button(self):
        self.click_on_element(PasswordRecoveryPageLocators.SHOW_HIDDEN_BUTTON)
        return PasswordRecoveryPageLocators.ACTIV_FIELD_PASSWORD

    def add_email(self):
        self.add_text(BasePageLocators.EMAIL_INPUT, UserData.EMAIL)
