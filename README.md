# Sprint 6 - Автотесты для Яндекс.Самокат

Автоматизация UI-тестирования сервиса аренды самокатов.

## Технологии

- Python 3.10+
- Selenium WebDriver
- Pytest
- Allure
- Firefox
- Page Object Model

## Установка

```bash
pip install -r requirements.txt
brew install geckodriver  # для macOS
```

## Запуск тестов

```bash
pytest tests/
```

## Allure отчёт

```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Структура

- `pages/` - Page Object классы
- `locators/` - локаторы элементов
- `tests/` - тестовые сценарии
- `helpers/` - тестовые данные
