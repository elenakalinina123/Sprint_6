import allure

from ..locators import index_locators
from ..pages.base_page import BasePage


class IndexPage(BasePage):
    page_link = index_locators.page_link

    @allure.step('Загружаем главную страницу')
    def load_index_page(self):
        self.load(self.page_link)

    @allure.step('выдаём адрес главной страницы')
    def get_page_link(self):
        return index_locators.page_link

    @allure.step('нажимаем кнопку согласиться с куки')
    def click_consent_cookies(self):
        button = self.find_element(
            index_locators.cookie_consent_button)

        self.wait_until_element_is_clickable(button)

        button.click()

    @allure.step('нажимаем верхнюю кнопку заказа')
    def click_order_top(self):
        order_button = self.find_element(index_locators.order_top)
        order_button.location_once_scrolled_into_view

        self.wait_until_element_is_clickable(order_button)

        self.click_object(order_button)

    @allure.step('нажимаем нижнюю кнопку заказа')
    def click_order_bottom(self):
        order_button = self.find_element(index_locators.order_bottom)
        order_button.location_once_scrolled_into_view

        self.wait_until_element_is_clickable(order_button)

        self.click_object(order_button)

    @allure.step('нажимаем {n}-ю кнопку заказа')
    def click_order_top_or_bottom(self, n):
        buttons = [self.click_order_top, self.click_order_bottom]
        buttons[n]()
