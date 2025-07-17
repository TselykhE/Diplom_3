from selenium.webdriver.common.by import By


class PersonalAccountPageLoc:

    PA_HISTORY_ORDER_BUTTON = By.XPATH, '//a[@href="/account/order-history"]'
    PA_EXIT_BUTTON = By.XPATH, './/button[text()="Выход"]'
    PA_ORDER_NUMBER_HISTORY = By.XPATH, '(//p[@class="text text_type_digits-default"])[1]'
