from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы оформления заказа"""
    
    # Форма "Для кого самокат"
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@class='select-search__input']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    # Кнопка "Далее" на первой форме
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Форма "Про аренду"
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']")
    
    # Варианты срока аренды
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    RENTAL_PERIOD_THREE_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")
    RENTAL_PERIOD_FOUR_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    RENTAL_PERIOD_FIVE_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")
    RENTAL_PERIOD_SIX_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']")
    RENTAL_PERIOD_SEVEN_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")
    
    # Чекбоксы цвета самоката
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    
    # Поле комментария
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопка "Заказать" на второй форме
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    
    # Модальное окно подтверждения
    CONFIRM_ORDER_MODAL = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Модальное окно успешного заказа
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
