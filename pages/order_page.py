import allure

from ..locators import order_locators
from ..pages.base_page import BasePage


class OrderPage(BasePage):
    page_link = order_locators.page_link

    @allure.step('Загружаем страницу заказа')
    def load_order_page(self):
        self.load(self.page_link)

    @allure.step('выдаём адрес страницы заказа')
    def get_page_link(self):
        return order_locators.page_link

    @allure.step('нажимаем кнопку Яндекс')
    def click_yandex(self):
        self.find_element(order_locators.yandex).click()

    @allure.step('нажимаем кнопку Самокат')
    def click_samokat(self):
        self.find_element(order_locators.samokat).click()

    @allure.step('Заполняем имя')
    def set_first_name(self, first_name):
        field = self.find_element(order_locators.first_name)
        field.send_keys(first_name)

    @allure.step('Заполняем фамилию')
    def set_last_name(self, last_name):
        field = self.find_element(order_locators.last_name)
        field.send_keys(last_name)

    @allure.step('Заполняем адрес')
    def set_address(self, address):
        field = self.find_element(order_locators.address)
        field.send_keys(address)

    @allure.step('Заполняем станцию метро')
    def set_metro(self, station_number):
        field = self.find_element(order_locators.metro)
        field.click()
        options = [order_locators.metro_10_button,
                   order_locators.metro_20_button]
        option = self.find_element(options[station_number])
        option.location_once_scrolled_into_view
        self.wait_until_element_is_clickable(option)
        option.click()

    @allure.step('Заполняем телефон')
    def set_phone(self, phone):
        field = self.find_element(order_locators.phone)
        field.send_keys(phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next(self):
        next_button = self.find_element(order_locators.next_button)
        next_button.location_once_scrolled_into_view
        self.wait_until_element_is_clickable(next_button)
        next_button.click()

    @allure.step('Устанавливаем дату')
    def set_date(self, date):
        field = self.find_element(order_locators.date)
        field.send_keys(date)
        self.find_element(order_locators.date_5th).click()

    @allure.step('Устанавливаем длительность')
    def set_duration(self):
        self.find_element(order_locators.duration).click()
        self.find_element(order_locators.duration_one_day).click()

    @allure.step('нажимаем чекбокс серый цвет')
    def set_grey_color(self):
        self.find_element(order_locators.grey_color).click()

    @allure.step('нажимаем чекбокс черный цвет')
    def set_black_color(self):
        self.find_element(order_locators.black_color).click()

    @allure.step('Заполняем комментарий к заказу')
    def set_comment(self, comment):
        field = self.find_element(order_locators.comment)
        field.click()
        field.send_keys(comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order(self):
        self.find_element(order_locators.order_button).click()

    @allure.step('Нажимаем кнопку "Да"')
    def click_yes(self):
        self.find_element(order_locators.yes_button).click()

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
        popup = self.find_element(order_locators.order_confirmation)
        return popup.is_displayed()

    @allure.step('нажимаем кнопку согласиться с куки')
    def click_consent_cookies(self):
        button = self.find_element(
            order_locators.cookie_consent_button)

        self.wait_until_element_is_clickable(button)

        button.click()

    @allure.step('проверяем что кнопка куков не видна')
    def cookies_not_visible(self):
        return self.invisility_of_elememnt_located(
            order_locators.cookie_consent_button
        )
