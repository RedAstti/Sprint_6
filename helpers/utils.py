"""Вспомогательные утилиты для работы с веб-элементами"""

import random
import string
from datetime import datetime, timedelta


def generate_random_phone():
    """Генерация случайного номера телефона"""
    return f"+7999{random.randint(1000000, 9999999)}"


def generate_random_name():
    """Генерация случайного имени"""
    names = ["Иван", "Петр", "Сергей", "Алексей", "Дмитрий", "Мария", "Анна", "Елена", "Ольга"]
    return random.choice(names)


def generate_random_last_name():
    """Генерация случайной фамилии"""
    last_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Иванова", "Петрова", "Сидорова"]
    return random.choice(last_names)


def generate_random_address():
    """Генерация случайного адреса"""
    streets = ["Ленина", "Пушкина", "Гагарина", "Мира", "Победы"]
    street = random.choice(streets)
    house = random.randint(1, 100)
    apartment = random.randint(1, 200)
    return f"Москва, ул. {street}, д. {house}, кв. {apartment}"


def generate_future_date(days_ahead=1):
    """
    Генерация будущей даты
    :param days_ahead: количество дней вперед
    :return: дата в формате дд.мм.гггг
    """
    future_date = datetime.now() + timedelta(days=days_ahead)
    return future_date.strftime("%d.%m.%Y")


def generate_random_comment():
    """Генерация случайного комментария для заказа"""
    comments = [
        "Позвоните за час",
        "Оставить у консьержа",
        "Домофон не работает",
        "Привезти до 18:00",
        "Без звонка не открывать"
    ]
    return random.choice(comments)
