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

        assert order.cookies_not_visible()

    @allure.title('Тест позитивного флоу заказа самоката')
    @pytest.mark.parametrize('data_set', [0, 1])
    def test_order_confirmation(self, driver, data_set):
        order = OrderPage(driver)

        order.load_order_page()

        order.input_form(*form_data[data_set])

        assert order.order_confirmation_visible()
