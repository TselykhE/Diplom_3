from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLoc


class PersonalAccountPage(BasePage):

    def click_on_history_button(self):
        self.click_on_element(PersonalAccountPageLoc.PA_HISTORY_ORDER_BUTTON)

    def click_on_exit_button(self):
        self.click_on_element(PersonalAccountPageLoc.PA_EXIT_BUTTON)

    def order_number_history(self):
        return self.text_element(PersonalAccountPageLoc.PA_ORDER_NUMBER_HISTORY)
