import allure
import pytest

from data import ANSWERS
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка ответа на вопрос')
    @allure.description('Проверяем, что при клике на вопрос, ответ соответствует ожидаемому')
    @pytest.mark.parametrize(
        'num_q, answer',
        [
            (0, ANSWERS[0]),
            (1, ANSWERS[1]),
            (2, ANSWERS[2]),
            (3, ANSWERS[3]),
            (4, ANSWERS[4]),
            (5, ANSWERS[5]),
            (6, ANSWERS[6]),
            (7, ANSWERS[7])
        ]
    )
    def test_check_answer_to_question(self, driver, num_q, answer):
        main_page = MainPage(driver)
        assert main_page.get_text_answer_to_question(num_q) == answer
