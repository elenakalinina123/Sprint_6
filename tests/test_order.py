import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..pages.base_page import BasePage
from ..pages.index_page import IndexPage
from ..pages.order_page import OrderPage


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('order_button', [0, 1])
    def test_points_of_entry(self, order_button):
        index = IndexPage(self.driver)
        order = OrderPage(self.driver)

        index.load_index_page()
        index.click_order_top_or_bottom(order_button)

        assert self.driver.current_url == order.get_page_link()

    def test_consent_cookies(self):
        order = OrderPage(self.driver)

        order.click_consent_cookies()

        assert True

    @pytest.mark.parametrize('data_set', [0, 1])
    def test_order_confirmation(self, form_data, data_set):
        order = OrderPage(self.driver)

        order.load_order_page()

        order.input_form(*form_data[data_set])

        assert order.order_confirmation_visible()

    def test_samokat(self):
        order = OrderPage(self.driver)
        index = IndexPage(self.driver)
        base = BasePage(self.driver)

        order.load_order_page()
        base.click_samokat()

        assert self.driver.current_url == index.get_page_link()

    def test_yandex(self):
        order = OrderPage(self.driver)
        base = BasePage(self.driver)

        wait = WebDriverWait(self.driver, 10)

        order.load_order_page()

        original_window = self.driver.current_window_handle

        assert len(self.driver.window_handles) == 1

        base.click_yandex()

        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        wait.until(EC.url_contains("dzen.ru"))

        assert 'dzen.ru' in self.driver.current_url
