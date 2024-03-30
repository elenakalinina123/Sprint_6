import allure

from ..locators import base_locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку Самоката')
    def click_samokat(self):
        samokat = self.driver.find_element(*base_locators.samokat)
        samokat.click()

    @allure.step('Нажимаем кнопку Яндекса')
    def click_yandex(self):
        yandex = self.driver.find_element(*base_locators.yandex)
        yandex.click()

    @allure.step('Нажимаем кнопку заказа (верхнюю)')
    def click_order_top(self):
        order_button = self.driver.find_element(*base_locators.order_top)
        order_button.click()
