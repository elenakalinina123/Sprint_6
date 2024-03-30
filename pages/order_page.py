import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import order_locators


class OrderPage:
    @allure.step("Создаём драйвер")
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу заказа')
    def load_order_page(self):
        self.driver.get(order_locators.order_page_link)

    def get_page_link(self):
        return order_locators.order_page_link

    @allure.step('Заполняем имя')
    def set_first_name(self, first_name):
        field = self.driver.find_element(*order_locators.first_name)
        field.send_keys(first_name)

    @allure.step('Заполняем фамилию')
    def set_last_name(self, last_name):
        field = self.driver.find_element(*order_locators.last_name)
        field.send_keys(last_name)

    @allure.step('Заполняем адрес')
    def set_address(self, address):
        field = self.driver.find_element(*order_locators.address)
        field.send_keys(address)

    @allure.step('Заполняем станцию метро')
    def set_metro(self, station_number):
        field = self.driver.find_element(*order_locators.metro)
        field.click()
        options = [order_locators.metro_10_button,
                   order_locators.metro_20_button]
        option = self.driver.find_element(*options[station_number])
        option.location_once_scrolled_into_view

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(option))
        option.click()

    @allure.step('Заполняем телефон')
    def set_phone(self, phone):
        field = self.driver.find_element(*order_locators.phone)
        field.send_keys(phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next(self):
        next_button = self.driver.find_element(*order_locators.next_button)
        next_button.location_once_scrolled_into_view
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(next_button))
        next_button.click()

    @allure.step('Устанавливаем дату')
    def set_date(self, date):
        field = self.driver.find_element(*order_locators.date)
        field.send_keys(date)
        self.driver.find_element(*order_locators.date_5th).click()

    @allure.step('Устанавливаем длительность')
    def set_duration(self):
        self.driver.find_element(*order_locators.duration).click()
        self.driver.find_element(*order_locators.duration_one_day).click()

    def set_grey_color(self):
        self.driver.find_element(*order_locators.grey_color).click()

    def set_black_color(self):
        self.driver.find_element(*order_locators.black_color).click()

    @allure.step('Заполняем комментарий к заказу')
    def set_comment(self, comment):
        field = self.driver.find_element(*order_locators.comment)
        field.click()
        field.send_keys(comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order(self):
        self.driver.find_element(*order_locators.order_button).click()

    @allure.step('Нажимаем кнопку "Да"')
    def click_yes(self):
        self.driver.find_element(*order_locators.yes_button).click()

    @allure.step('Заполняем форму заказа')
    def input_form(
            self, first_name, last_name, address, metro, phone, date, comment):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next()
        self.set_date(date)
        self.set_duration()
        self.set_black_color()
        self.set_comment(comment)
        self.click_order()
        self.click_yes()

    @allure.step('Проверка видимости подтверждения заказа')
    def order_confirmation_visible(self):
        popup = self.driver.find_element(*order_locators.order_confirmation)
        return popup.is_displayed()

    def click_consent_cookies(self):
        button = self.driver.find_element(
            *order_locators.cookie_consent_button)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button))

        button.click()
