import allure
import pytest

from ..data import faq_test_data
from ..pages.index_page import IndexPage


class TestFAQ:
    @allure.title('Тест вопросов и ответов')
    @pytest.mark.parametrize('test_data', faq_test_data)
    def test_questions(self, driver, test_data):
        question_locator, answer_locator, text = test_data

        index = IndexPage(driver)
        index.load_index_page()

        index.click(question_locator)
        answer = index.wait_until_visibility(answer_locator)

        assert answer.text == text
