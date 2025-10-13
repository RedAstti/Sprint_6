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
        """
        Тест проверяет:
        1. Переход на страницу заказа
        2. Клик на логотип Самоката
        3. Возврат на главную страницу
        """
        main_page = MainPage(driver)

        # Переходим на страницу заказа через кнопку
        main_page.click_order_button_top()

        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()

        # Проверяем, что вернулись на главную страницу
        current_url = main_page.get_current_url()
        assert current_url == BASE_URL or current_url == f"{BASE_URL}/", \
            f"Не произошел переход на главную страницу. Текущий URL: {current_url}"

    @allure.title("Переход на Дзен по клику на логотип 'Яндекса'")
    @allure.description("Проверяем, что клик на логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """
        Тест проверяет:
        1. Клик на логотип Яндекса
        2. Открытие нового окна
        3. Переход на страницу Дзена
        """
        main_page = MainPage(driver)

        # Запоминаем количество окон до клика
        windows_before = main_page.get_window_handles_count()

        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()

        # Переключаемся на новое окно
        main_page.switch_to_new_window()

        # Проверяем, что открылось новое окно
        windows_after = main_page.get_window_handles_count()
        assert windows_after > windows_before, \
            "Новое окно не открылось после клика на логотип Яндекса"

        # Проверяем, что открылась страница Дзен
        dzen_page = DzenPage(driver)
        
        # Ждем перенаправления на Дзен (может быть редирект)
        import time
        time.sleep(3)  # Даем время на редирект
        
        assert dzen_page.is_dzen_page_opened(), \
            f"Не произошел переход на страницу Дзен. Текущий URL: {dzen_page.get_current_url()}"
