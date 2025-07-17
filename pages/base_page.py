import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seletools.actions import drag_and_drop
from locators.base_page_locators import BasePageLocators
from data import UserData


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Переход по урлу')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием')
    def find_element_and_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов с ожиданием')
    def find_elements_and_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Ожидание скрытия элемента')
    def wait_for_invisibility_of_element(self, locator):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.wait_for_page_load()
        self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавить текст')
    def add_text(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    @allure.step('Получить текущий урл')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание загрузки страницы')
    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Получить текст элемента')
    def text_element(self, locator):
        return self.find_element_and_wait(locator).text

    @allure.step('Получить класс элемента')
    def class_element(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("class")

    @allure.step('Заполнить поле авторизации')
    def add_auth_field_click(self, email: str = UserData.EMAIL,
                             password: str = UserData.PASSWORD):
        self.add_text(BasePageLocators.EMAIL_INPUT, email)
        self.add_text(BasePageLocators.PASSWORD_INPUT, password)
        self.click_on_element(BasePageLocators.LOG_IN_BUTTON)

    @allure.step('Найти кнопку регистрации')
    def find_log_in_button(self):
        self.find_element_and_wait(BasePageLocators.LOG_IN_BUTTON)
