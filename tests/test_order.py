import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers.test_data import ORDER_DATA_1, ORDER_DATA_2


@allure.suite("Оформление заказа")
class TestOrderScooter:
    """Тесты для проверки оформления заказа самоката"""

    @allure.title("Заказ самоката через верхнюю кнопку")
    @allure.description("Проверяем полный флоу оформления заказа через верхнюю кнопку 'Заказать'")
    def test_order_scooter_top_button(self, driver):
        """Тест оформления заказа через верхнюю кнопку 'Заказать'"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button_top()

        order_page.fill_customer_form(
            first_name=ORDER_DATA_1["first_name"],
            last_name=ORDER_DATA_1["last_name"],
            address=ORDER_DATA_1["address"],
            metro_station=ORDER_DATA_1["metro_station"],
            phone=ORDER_DATA_1["phone"]
        )

        order_page.click_next_button()

        order_page.input_delivery_date(ORDER_DATA_1["delivery_date"])
        order_page.select_rental_period(ORDER_DATA_1["rental_period"])
        order_page.select_color(ORDER_DATA_1["color"])
        order_page.input_comment(ORDER_DATA_1["comment"])

        order_page.click_order_button()
        order_page.confirm_order()

        # Собираем данные до проверок
        is_message_displayed = order_page.is_success_message_displayed()
        success_text = order_page.get_success_message_text()

        # Проверки
        assert is_message_displayed, "Сообщение об успешном создании заказа не отображается"
        assert "Заказ оформлен" in success_text, \
            f"Текст сообщения не содержит 'Заказ оформлен'. Получено: '{success_text}'"

    @allure.title("Заказ самоката через нижнюю кнопку")
    @allure.description("Проверяем полный флоу оформления заказа через нижнюю кнопку 'Заказать'")
    def test_order_scooter_bottom_button(self, driver):
        """Тест оформления заказа через нижнюю кнопку 'Заказать'"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button_bottom()

        order_page.fill_customer_form(
            first_name=ORDER_DATA_2["first_name"],
            last_name=ORDER_DATA_2["last_name"],
            address=ORDER_DATA_2["address"],
            metro_station=ORDER_DATA_2["metro_station"],
            phone=ORDER_DATA_2["phone"]
        )

        order_page.click_next_button()

        order_page.input_delivery_date(ORDER_DATA_2["delivery_date"])
        order_page.select_rental_period(ORDER_DATA_2["rental_period"])
        order_page.select_color(ORDER_DATA_2["color"])
        order_page.input_comment(ORDER_DATA_2["comment"])

        order_page.click_order_button()
        order_page.confirm_order()

        # Собираем данные до проверок
        is_message_displayed = order_page.is_success_message_displayed()
        success_text = order_page.get_success_message_text()

        # Проверки
        assert is_message_displayed, "Сообщение об успешном создании заказа не отображается"
        assert "Заказ оформлен" in success_text, \
            f"Текст сообщения не содержит 'Заказ оформлен'. Получено: '{success_text}'"
