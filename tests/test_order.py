import allure
import pytest

from ..data import form_data
from ..pages.index_page import IndexPage
from ..pages.order_page import OrderPage


class TestOrder:
    @allure.title('Тест двух точек входа в флоу заказа')
    @pytest.mark.parametrize('order_button', [0, 1])
    def test_points_of_entry(self, driver, order_button):
        index = IndexPage(driver)
        order = OrderPage(driver)

        index.load_index_page()
        index.click_order_top_or_bottom(order_button)

        assert order.get_current_url() == order.get_page_link()

    @allure.title('Нажимаем кнопку куков')
    def test_consent_cookies(self, driver):
        order = OrderPage(driver)

        order.click_consent_cookies()

        assert True

    @allure.title('Тест позитивного флоу заказа самоката')
    @pytest.mark.parametrize('data_set', [0, 1])
    def test_order_confirmation(self, driver, data_set):
        order = OrderPage(driver)

        order.load_order_page()

        order.input_form(*form_data[data_set])

        assert order.order_confirmation_visible()

    @allure.title('Тест перехода на главную страницу сайта')
    def test_samokat(self, driver):
        order = OrderPage(driver)
        index = IndexPage(driver)

        order.load_order_page()
        order.click_samokat()

        assert order.get_current_url() == index.get_page_link()

    @allure.title('Тест перехода на Яндекс Дзен')
    def test_yandex(self, driver):
        order = OrderPage(driver)

        order.load_order_page()

        original_window = order.get_current_window_handle()

        assert len(order.window_handles()) == 1

        order.click_yandex()

        order.switch_to_other_window(original_window)

        order.wait_until_url_contains('dzen.ru')

        assert 'dzen.ru' in order.get_current_url()
