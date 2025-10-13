import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        """Кликнуть на кнопку 'Заказать' в шапке"""
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    @allure.step("Прокрутить до нижней кнопки 'Заказать' и кликнуть")
    def click_order_button_bottom(self):
        """Прокрутить до кнопки 'Заказать' внизу страницы и кликнуть"""
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на логотип 'Самоката'")
    def click_scooter_logo(self):
        """Кликнуть на логотип Самоката"""
        self.click_element(self.locators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип 'Яндекса'")
    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекса"""
        self.click_element(self.locators.YANDEX_LOGO)

    @allure.step("Прокрутить до раздела 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        """Прокрутить страницу до раздела FAQ"""
        self.scroll_to_element(self.locators.FAQ_SECTION)

    @allure.step("Кликнуть на вопрос #{question_index}")
    def click_faq_question(self, question_index):
        """
        Кликнуть на вопрос в разделе FAQ
        :param question_index: индекс вопроса (0-7)
        """
        question_locator = getattr(self.locators, f"FAQ_QUESTION_{question_index}")
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step("Получить текст ответа на вопрос #{question_index}")
    def get_faq_answer_text(self, question_index):
        """
        Получить текст ответа на вопрос
        :param question_index: индекс вопроса (0-7)
        :return: текст ответа
        """
        answer_locator = getattr(self.locators, f"FAQ_ANSWER_{question_index}")
        self.wait_for_element_visibility(answer_locator)
        return self.get_text(answer_locator)

    @allure.step("Проверить видимость ответа на вопрос #{question_index}")
    def is_faq_answer_visible(self, question_index):
        """
        Проверить, виден ли ответ на вопрос
        :param question_index: индекс вопроса (0-7)
        :return: True если виден, False если нет
        """
        answer_locator = getattr(self.locators, f"FAQ_ANSWER_{question_index}")
        return self.is_element_visible(answer_locator)
