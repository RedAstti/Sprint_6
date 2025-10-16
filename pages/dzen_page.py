import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators


class DzenPage(BasePage):
    """Класс для работы со страницей Яндекс.Дзен"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DzenPageLocators

    @allure.step("Проверить, что открылась страница Дзен")
    def is_dzen_page_opened(self):
        """Проверить, что открылась страница Дзен по URL"""
        return "dzen.ru" in self.get_current_url() or "ya.ru" in self.get_current_url()

    @allure.step("Дождаться загрузки страницы Дзен")
    def wait_for_dzen_page_load(self):
        """Ждать появления элемента на странице Дзен"""
        self.wait_for_url_contains("dzen.ru", timeout=10)
