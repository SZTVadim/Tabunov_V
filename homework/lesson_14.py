"""
Тема: Функции и условные конструкции в Python
"""

# ЗАДАНИЕ 1: Функции и условия

# 1. Создайте функцию calculate_total(price, tax_percent):
#    - возвращает итоговую цену с налогом
#    - если налог > 20% или цена < 0, возвращает сообщение об ошибке


def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return "Ошибка: неверные данные"

    tax_amount = price * tax_percent / 100
    total_price = price + tax_amount
    return total_price

# 2. Создайте функцию get_level(points):
#    - points >= 100 → "Эксперт"
#    - points >= 50 → "Продвинутый"
#    - points >= 20 → "Начинающий"
#    - иначе → "Новичок"


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"

# ЗАДАНИЕ 2: Функции с условиями и match/case

# 1. Создайте функцию process_status(status) с match/case:
#    - "active" → "Статус активен"
#    - "inactive" → "Статус неактивен"
#    - "pending" → "Статус в ожидании"
#    - "blocked" → "Статус заблокирован"
#    - иначе → "Неизвестный статус"


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
