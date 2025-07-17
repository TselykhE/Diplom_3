from selenium.webdriver.common.by import By


class BasePageLocators:

    LOG_IN_ACCOUNT_MAIN = By.XPATH, './/button[text()="Войти в аккаунт"]'
    LOG_IN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    EMAIL_INPUT = By.XPATH, './/label[text()="Email"]/following-sibling::input[@name="name"]'
    PASSWORD_INPUT = By.XPATH, './/label[text()="Пароль"]/following-sibling::input[@name="Пароль"]'
    PROBLEM_MODAL = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'
