import allure

from ..pages.index_page import IndexPage
from ..pages.order_page import OrderPage


class TestRedirect:
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
