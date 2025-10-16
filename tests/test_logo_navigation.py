import pytest
import allure
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from urls import BASE_URL


@allure.suite("Навигация по логотипам")
class TestLogoNavigation:
    """Тесты для проверки навигации через логотипы"""

    @allure.title("Переход на главную страницу по клику на логотип 'Самоката'")
    @allure.description("Проверяем, что клик на логотип Самоката возвращает на главную страницу")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        """Тест проверяет переход на главную страницу по логотипу Самоката"""
        main_page = MainPage(driver)

        main_page.click_order_button_top()
        main_page.click_scooter_logo()

        current_url = main_page.get_current_url()
        assert current_url == BASE_URL or current_url == f"{BASE_URL}/", \
            f"Не произошел переход на главную страницу. Текущий URL: {current_url}"

    @allure.title("Открытие нового окна по клику на логотип 'Яндекса'")
    @allure.description("Проверяем, что клик на логотип Яндекса открывает новое окно")
    def test_yandex_logo_opens_new_window(self, driver):
        """Тест проверяет открытие нового окна по логотипу Яндекса"""
        main_page = MainPage(driver)

        windows_before = main_page.get_window_handles_count()
        main_page.click_yandex_logo()
        windows_after = main_page.get_window_handles_count()

        assert windows_after > windows_before, \
            "Новое окно не открылось после клика на логотип Яндекса"

    @allure.title("Переход на Дзен по клику на логотип 'Яндекса'")
    @allure.description("Проверяем, что клик на логотип Яндекса открывает страницу Дзен")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """Тест проверяет переход на страницу Дзен по логотипу Яндекса"""
        main_page = MainPage(driver)
        dzen_page = DzenPage(driver)

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        dzen_page.wait_for_dzen_page_load()

        is_dzen_opened = dzen_page.is_dzen_page_opened()

        assert is_dzen_opened, \
            f"Не произошел переход на страницу Дзен. Текущий URL: {dzen_page.get_current_url()}"
