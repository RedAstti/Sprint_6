import pytest
import allure
from pages.main_page import MainPage
from helpers.test_data import FAQ_EXPECTED_ANSWERS


@allure.suite("Раздел 'Вопросы о важном'")
class TestFAQSection:
    """Тесты для проверки раздела 'Вопросы о важном'"""

    @allure.title("Проверка раскрытия вопроса #{question_index}")
    @allure.description("Проверяем, что при клике на вопрос открывается соответствующий текст ответа")
    @pytest.mark.parametrize("question_index,expected_answer", [
        (0, FAQ_EXPECTED_ANSWERS[0]),
        (1, FAQ_EXPECTED_ANSWERS[1]),
        (2, FAQ_EXPECTED_ANSWERS[2]),
        (3, FAQ_EXPECTED_ANSWERS[3]),
        (4, FAQ_EXPECTED_ANSWERS[4]),
        (5, FAQ_EXPECTED_ANSWERS[5]),
        (6, FAQ_EXPECTED_ANSWERS[6]),
        (7, FAQ_EXPECTED_ANSWERS[7])
    ])
    def test_faq_question_answer(self, driver, question_index, expected_answer):
        """
        Тест проверяет раскрытие вопроса и соответствие текста ответа
        """
        main_page = MainPage(driver)
        
        # Прокрутить до раздела FAQ
        main_page.scroll_to_faq_section()
        
        # Кликнуть на вопрос
        main_page.click_faq_question(question_index)
        
        # Проверить, что ответ отображается
        assert main_page.is_faq_answer_visible(question_index), \
            f"Ответ на вопрос {question_index} не отображается"
        
        # Проверить текст ответа
        actual_answer = main_page.get_faq_answer_text(question_index)
        assert expected_answer in actual_answer, \
            f"Текст ответа не соответствует ожидаемому. Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
