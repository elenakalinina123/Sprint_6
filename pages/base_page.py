import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    page_link = None
    driver = None

    @allure.step('инициализируем BasePage')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу {link}')
    def load(self, link):
        self.driver.get(link)

    @allure.step('ждем {time} секунд')
    def wait(self, time):
        wait = WebDriverWait(self.driver, time)
        return wait

    @allure.step('ждём видимости элемента')
    def wait_until_visibility(self, locator):
        return self.wait(10).until(
            EC.visibility_of_element_located(locator))

    @allure.step('ждём пока url не станет включать в себя {string}')
    def wait_until_url_contains(self, string):
        return self.wait(10).until(EC.url_contains(string))

    @allure.step('находим элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('проверяем текущий url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('проверям текущее имя окна')
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step('проверяем список окон')
    def window_handles(self):
        return self.driver.window_handles

    @allure.step('переключаемся на окно {handle}')
    def switch_to_handle(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step('кликаем по локатору')
    def click(self, locator):
        button = self.wait(10).until(EC.element_to_be_clickable(locator))
        button.location_once_scrolled_into_view
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('кликаем по объекту')
    def click_object(self, button):
        self.driver.execute_script("arguments[0].click();", button)

    def switch_to_other_window(self, old_handle):

        self.wait(10).until(EC.number_of_windows_to_be(2))

        for window_handle in self.window_handles():
            if window_handle != old_handle:
                self.switch_to_handle(window_handle)
                break
