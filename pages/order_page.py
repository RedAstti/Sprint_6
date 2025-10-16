import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    """Класс для работы со страницей оформления заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Заполнить форму 'Для кого самокат': {first_name} {last_name}, {address}, метро {metro_station}, {phone}")
    def fill_customer_form(self, first_name, last_name, address, metro_station, phone):
        """Заполнить первую форму заказа"""
        self.wait_for_element_visibility(self.locators.FIRST_NAME_INPUT, timeout=15)
        self.input_text(self.locators.FIRST_NAME_INPUT, first_name)
        self.input_text(self.locators.LAST_NAME_INPUT, last_name)
        self.input_text(self.locators.ADDRESS_INPUT, address)
        
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

    @allure.step("Ввести дату доставки: {delivery_date}")
    def input_delivery_date(self, delivery_date):
        """Ввести дату доставки"""
        self.input_text(self.locators.DELIVERY_DATE_INPUT, delivery_date)
        self.find_element(self.locators.DELIVERY_DATE_INPUT).send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {rental_period}")
    def select_rental_period(self, rental_period):
        """Выбрать срок аренды из выпадающего списка"""
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
        
        period_locator = rental_period_mapping[rental_period]
        self.click_element(period_locator)

    @allure.step("Выбрать цвет: {color}")
    def select_color(self, color):
        """Выбрать цвет самоката"""
        color_mapping = {
            "black": self.locators.COLOR_BLACK_CHECKBOX,
            "grey": self.locators.COLOR_GREY_CHECKBOX
        }
        color_locator = color_mapping[color]
        self.click_element(color_locator)

    @allure.step("Ввести комментарий: {comment}")
    def input_comment(self, comment):
        """Ввести комментарий для курьера"""
        self.input_text(self.locators.COMMENT_INPUT, comment)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_order_button(self):
        """Кликнуть на кнопку 'Заказать'"""
        self.click_element(self.locators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        self.wait_for_element_visibility(self.locators.CONFIRM_ORDER_MODAL)
        self.click_element(self.locators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить успешное создание заказа")
    def is_success_message_displayed(self):
        """Проверить отображение сообщения об успехе"""
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE, timeout=10)

    @allure.step("Получить текст сообщения об успехе")
    def get_success_message_text(self):
        """Получить текст сообщения об успешном заказе"""
        self.wait_for_element_visibility(self.locators.SUCCESS_MESSAGE)
        return self.get_text(self.locators.SUCCESS_MESSAGE)
