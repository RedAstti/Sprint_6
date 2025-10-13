import allure
from pages.base_page import BasePage
from locators.locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    """Класс для работы со страницей оформления заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Заполнить форму 'Для кого самокат': {first_name} {last_name}, {address}, метро {metro_station}, {phone}")
    def fill_customer_form(self, first_name, last_name, address, metro_station, phone):
        """
        Заполнить первую форму заказа (Для кого самокат)
        :param first_name: Имя
        :param last_name: Фамилия
        :param address: Адрес доставки
        :param metro_station: Станция метро
        :param phone: Номер телефона
        """
        self.wait_for_element_visibility(self.locators.FIRST_NAME_INPUT, timeout=15)
        self.input_text(self.locators.FIRST_NAME_INPUT, first_name)
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        self.input_text(self.locators.ADDRESS_INPUT, address)
        
        # Ввод метро с ожиданием подсказок
        metro_input = self.find_element(self.locators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)
        self.driver.implicitly_wait(1)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        
        self.input_text(self.locators.PHONE_INPUT, phone)

    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_next_button(self):
        """Кликнуть на кнопку 'Далее'"""
        self.click_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду': дата {delivery_date}, срок {rental_period}, цвет {color}")
    def fill_rental_form(self, delivery_date, rental_period, color=None, comment=""):
        """
        Заполнить вторую форму заказа (Про аренду)
        :param delivery_date: Дата доставки (формат: дд.мм.гггг)
        :param rental_period: Срок аренды (например, "сутки", "двое суток")
        :param color: Цвет самоката ("black", "grey" или None)
        :param comment: Комментарий для курьера
        """
        # Ввод даты доставки
        self.input_text(self.locators.DELIVERY_DATE_INPUT, delivery_date)
        self.find_element(self.locators.DELIVERY_DATE_INPUT).send_keys(Keys.ENTER)
        
        # Выбор срока аренды
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        
        rental_period_mapping = {
            "сутки": self.locators.RENTAL_PERIOD_ONE_DAY,
            "двое суток": self.locators.RENTAL_PERIOD_TWO_DAYS,
            "трое суток": self.locators.RENTAL_PERIOD_THREE_DAYS,
            "четверо суток": self.locators.RENTAL_PERIOD_FOUR_DAYS,
            "пятеро суток": self.locators.RENTAL_PERIOD_FIVE_DAYS,
            "шестеро суток": self.locators.RENTAL_PERIOD_SIX_DAYS,
            "семеро суток": self.locators.RENTAL_PERIOD_SEVEN_DAYS
        }
        
        period_locator = rental_period_mapping.get(rental_period)
        if period_locator:
            self.click_element(period_locator)
        
        # Выбор цвета
        if color == "black":
            self.click_element(self.locators.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(self.locators.COLOR_GREY_CHECKBOX)
        
        # Комментарий
        if comment:
            self.input_text(self.locators.COMMENT_INPUT, comment)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_order_button(self):
        """Кликнуть на кнопку 'Заказать' во второй форме"""
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ (кликнуть 'Да')")
    def confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        self.wait_for_element_visibility(self.locators.CONFIRM_ORDER_MODAL)
        self.click_element(self.locators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить, что появилось сообщение об успешном создании заказа")
    def is_success_message_displayed(self):
        """
        Проверить, отображается ли сообщение об успешном создании заказа
        :return: True если сообщение видно, False если нет
        """
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE, timeout=10)

    @allure.step("Получить текст сообщения об успехе")
    def get_success_message_text(self):
        """Получить текст сообщения об успешном заказе"""
        self.wait_for_element_visibility(self.locators.SUCCESS_MESSAGE)
        return self.get_text(self.locators.SUCCESS_MESSAGE)
