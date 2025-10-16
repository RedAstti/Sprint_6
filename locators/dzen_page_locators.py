from selenium.webdriver.common.by import By


class DzenPageLocators:
    """Локаторы страницы Яндекс.Дзен"""
    
    DZEN_LOGO = (By.XPATH, "//a[contains(@aria-label, 'Дзен')]")
    DZEN_SEARCH = (By.XPATH, "//button[@aria-label='Поиск']")
