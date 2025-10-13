import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from urls import BASE_URL
import os


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия браузера Firefox
    Автоматически запускается перед каждым тестом и закрывается после
    """
    # Проверяем, есть ли geckodriver в PATH
    try:
        service = Service()
        browser = webdriver.Firefox(service=service)
    except Exception:
        # Если нет в PATH, пытаемся через webdriver-manager
        try:
            from webdriver_manager.firefox import GeckoDriverManager
            service = Service(GeckoDriverManager().install())
            browser = webdriver.Firefox(service=service)
        except Exception as e:
            raise Exception(
                "Не удалось найти geckodriver. Установите его:\n"
                "macOS: brew install geckodriver\n"
                "Linux: apt-get install firefox-geckodriver\n"
                f"Ошибка: {e}"
            )
    
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(BASE_URL)
    
    yield browser
    
    browser.quit()
