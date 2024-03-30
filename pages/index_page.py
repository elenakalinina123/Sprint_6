
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..locators import base_locators, index_locators

# from selenium.webdriver.support.wait import WebDriverWait


class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    def load_index_page(self):
        self.driver.get(index_locators.index_page_link)

    def get_page_link(self):
        return index_locators.index_page_link

    def click_order_top(self):
        order_button = self.driver.find_element(*base_locators.order_top)
        order_button.location_once_scrolled_into_view

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(order_button))

        order_button.click()

    def click_order_bottom(self):
        order_button = self.driver.find_element(*index_locators.order_bottom)
        order_button.location_once_scrolled_into_view

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(order_button))

        order_button.click()

    def click_order_top_or_bottom(self, n):
        buttons = [self.click_order_top, self.click_order_bottom]
        buttons[n]()

    def click_question_1(self):
        button = self.driver.find_element(*index_locators.question_1)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_2(self):
        button = self.driver.find_element(*index_locators.question_2)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_3(self):
        button = self.driver.find_element(*index_locators.question_3)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_4(self):
        button = self.driver.find_element(*index_locators.question_4)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_5(self):
        button = self.driver.find_element(*index_locators.question_5)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_6(self):
        button = self.driver.find_element(*index_locators.question_6)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_7(self):
        button = self.driver.find_element(*index_locators.question_7)
        button.location_once_scrolled_into_view
        button.click()

    def click_question_8(self):
        button = self.driver.find_element(*index_locators.question_8)
        button.location_once_scrolled_into_view
        button.click()

    def check_answer_1(self):  # хочется переписать через параметры
        answer = self.driver.find_element(*index_locators.answer_1)
        return EC.visibilityOf(answer)

    def check_answer_2(self):
        answer = self.driver.find_element(*index_locators.answer_2)
        return EC.visibilityOf(answer)

    def check_answer_3(self):
        answer = self.driver.find_element(*index_locators.answer_3)
        return EC.visibilityOf(answer)

    def check_answer_4(self):
        answer = self.driver.find_element(*index_locators.answer_4)
        return EC.visibilityOf(answer)

    def check_answer_5(self):
        answer = self.driver.find_element(*index_locators.answer_5)
        return EC.visibilityOf(answer)

    def check_answer_6(self):
        answer = self.driver.find_element(*index_locators.answer_6)
        return EC.visibilityOf(answer)

    def check_answer_7(self):
        answer = self.driver.find_element(*index_locators.answer_7)
        return EC.visibilityOf(answer)

    def check_answer_8(self):
        answer = self.driver.find_element(*index_locators.answer_8)
        return EC.visibilityOf(answer)
