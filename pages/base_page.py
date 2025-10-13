from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator, timeout=10):
        """Найти элемент на странице"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def find_element_clickable(self, locator, timeout=10):
        """Дождаться, пока элемент станет кликабельным"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator, timeout=10):
        """Кликнуть по элементу"""
        element = self.find_element_clickable(locator, timeout)
        try:
            element.click()
        except Exception:
            # Если обычный клик не работает, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_visible(self, locator, timeout=5):
        """Проверить, виден ли элемент"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def wait_for_url_contains(self, url_part, timeout=10):
        """Ждать, пока URL будет содержать указанную часть"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(url_part))

    def wait_for_element_visibility(self, locator, timeout=10):
        """Ждать, пока элемент станет видимым"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisibility(self, locator, timeout=10):
        """Ждать, пока элемент исчезнет"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    def switch_to_new_window(self):
        """Переключиться на новое окно"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def get_window_handles_count(self):
        """Получить количество открытых окон"""
        return len(self.driver.window_handles)
