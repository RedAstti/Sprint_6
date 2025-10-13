import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers.test_data import ORDER_DATA_1, ORDER_DATA_2


@allure.suite("Оформление заказа")
class TestOrderScooter:
    """Тесты для проверки оформления заказа самоката"""

    @allure.title("Заказ самоката через кнопку '{button_location}' с данными: {order_data[first_name]} {order_data[last_name]}")
    @allure.description("Проверяем полный флоу оформления заказа с проверкой успешного создания")
    @pytest.mark.parametrize("button_location,order_data", [
        ("верхняя", ORDER_DATA_1),
        ("нижняя", ORDER_DATA_2)
    ])
    def test_order_scooter_full_flow(self, driver, button_location, order_data):
        """
        Тест полного флоу оформления заказа:
        1. Клик на кнопку 'Заказать' (верхняя или нижняя)
        2. Заполнение формы 'Для кого самокат'
        3. Переход к форме 'Про аренду'
        4. Заполнение формы 'Про аренду'
        5. Подтверждение заказа
        6. Проверка сообщения об успешном создании заказа
        """
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Шаг 1: Клик на кнопку "Заказать"
        if button_location == "верхняя":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        # Шаг 2: Заполнить форму "Для кого самокат"
        order_page.fill_customer_form(
            first_name=order_data["first_name"],
            last_name=order_data["last_name"],
            address=order_data["address"],
            metro_station=order_data["metro_station"],
            phone=order_data["phone"]
        )

        # Шаг 3: Клик на кнопку "Далее"
        order_page.click_next_button()

        # Шаг 4: Заполнить форму "Про аренду"
        order_page.fill_rental_form(
            delivery_date=order_data["delivery_date"],
            rental_period=order_data["rental_period"],
            color=order_data["color"],
            comment=order_data["comment"]
        )

        # Шаг 5: Клик на кнопку "Заказать"
        order_page.click_order_button()

        # Шаг 6: Подтверждение заказа
        order_page.confirm_order()

        # Шаг 7: Проверка успешного создания заказа
        assert order_page.is_success_message_displayed(), \
            "Сообщение об успешном создании заказа не отображается"

        success_text = order_page.get_success_message_text()
        assert "Заказ оформлен" in success_text, \
            f"Текст сообщения не содержит 'Заказ оформлен'. Получено: '{success_text}'"
