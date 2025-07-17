from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    PASSWORD_RECOVERY_BUTTON = By.XPATH, './/a[@href="/forgot-password"]'
    RECOVERY_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    PASSWORD_RECOVERY_INPUT = By.XPATH, './/label[text()="Пароль"]'
    SHOW_HIDDEN_BUTTON = By.CLASS_NAME, 'input__icon.input__icon-action'
    ACTIV_FIELD_PASSWORD = By.XPATH, './/input[type()="text"]'
