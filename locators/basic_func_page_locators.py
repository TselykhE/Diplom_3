from selenium.webdriver.common.by import By

class BasicFuncPageLocators:

    LOG_IN_ACCOUNT_MAIN = By.XPATH, '//button[text()="Войти в аккаунт"]'
    PERSONAL_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]'
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_FEED_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]'
    INGREDIENT_BUTTON = By.CSS_SELECTOR, 'ul a:first-child img'
    MODAL_WINDOW = By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]'
    CLOSE_MODAL_WINDOW_BUTTON = By.XPATH, "//section[contains(@class, 'Modal_modal')]//button"
    BURGER_INGREDIENT = (By.CSS_SELECTOR, 'section[class*="BurgerConstructor_basket"]')
    INGREDIENT_CLOSE_MODAL_WINDOW = (By.CSS_SELECTOR, "div[class*='Modal_modal__container'] button")
    INGREDIENT_COUNTER = By.CSS_SELECTOR, "div.counter_counter__ZNLkj > p"
    ORDER_MODAL_WINDOW = (By.CSS_SELECTOR, 'button[class*="Modal_modal__close"]')
    NEW_NUMBER_ORDER = By.XPATH, ".//p[text()='Ваш заказ начали готовить']"
    ORDER_NUMBER_FROM_MODAL = By.XPATH, "//h2[contains(@class, 'text_type_digits-large') and starts-with(@class, 'Modal_modal__title')]"
