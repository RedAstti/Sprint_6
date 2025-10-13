import allure
from pages.base_page import BasePage
from locators.locators import DzenPageLocators


class DzenPage(BasePage):
    """Класс для работы со страницей Яндекс.Дзен"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DzenPageLocators

    @allure.step("Проверить, что открылась страница Дзен")
    def is_dzen_page_opened(self):
        """
        Проверить, что открылась страница Дзен
        :return: True если страница Дзен открыта
        """
        return "dzen.ru" in self.get_current_url() or "ya.ru" in self.get_current_url()
