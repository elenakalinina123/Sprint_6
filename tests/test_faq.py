from selenium import webdriver

from ..pages import index_page


class TestFAQ:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_question_1(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_1
        assert page.check_answer_1

    def test_question_2(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_2
        assert page.check_answer_2

    def test_question_3(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_3
        assert page.check_answer_3

    def test_question_4(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_4
        assert page.check_answer_4

    def test_question_5(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_5
        assert page.check_answer_5

    def test_question_6(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_6
        assert page.check_answer_6

    def test_question_7(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_7
        assert page.check_answer_7

    def test_question_8(self):
        page = index_page.IndexPage(self.driver)
        page.load_index_page()
        page.click_question_8
        assert page.check_answer_8
