from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    
    # Раздел "Вопросы о важном"
    FAQ_SECTION = (By.XPATH, "//div[@class='Home_FourPart__1uthg']")
    FAQ_HEADING = (By.XPATH, "//div[contains(@class, 'Home_FourPart')]//div[text()='Вопросы о важном']")
    
    # Вопросы (стрелочки для раскрытия)
    FAQ_QUESTION_0 = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_1 = (By.ID, "accordion__heading-1")
    FAQ_QUESTION_2 = (By.ID, "accordion__heading-2")
    FAQ_QUESTION_3 = (By.ID, "accordion__heading-3")
    FAQ_QUESTION_4 = (By.ID, "accordion__heading-4")
    FAQ_QUESTION_5 = (By.ID, "accordion__heading-5")
    FAQ_QUESTION_6 = (By.ID, "accordion__heading-6")
    FAQ_QUESTION_7 = (By.ID, "accordion__heading-7")
    
    # Ответы на вопросы
    FAQ_ANSWER_0 = (By.ID, "accordion__panel-0")
    FAQ_ANSWER_1 = (By.ID, "accordion__panel-1")
    FAQ_ANSWER_2 = (By.ID, "accordion__panel-2")
    FAQ_ANSWER_3 = (By.ID, "accordion__panel-3")
    FAQ_ANSWER_4 = (By.ID, "accordion__panel-4")
    FAQ_ANSWER_5 = (By.ID, "accordion__panel-5")
    FAQ_ANSWER_6 = (By.ID, "accordion__panel-6")
    FAQ_ANSWER_7 = (By.ID, "accordion__panel-7")


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


class DzenPageLocators:
    """Локаторы страницы Яндекс.Дзен"""
    
    # Логотип или элемент, подтверждающий, что мы на странице Дзен
    DZEN_LOGO = (By.XPATH, "//a[contains(@aria-label, 'Дзен')]")
    DZEN_SEARCH = (By.XPATH, "//button[@aria-label='Поиск']")
