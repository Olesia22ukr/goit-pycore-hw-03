from datetime import datetime

def get_days_from_today(date):
    """
    Обчислює кількість днів між заданою датою та сьогоднішнім днем.
    
    :param date: Рядок у форматі 'РРРР-ММ-ДД'
    :return: Ціле число, що показує різницю у днях (від'ємне, якщо дата у майбутньому)
    """
    try:
        # Конвертуємо вхідний рядок у дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримуємо поточну дату
        today_date = datetime.today().date()
        
        # Обчислюємо різницю у днях
        delta_days = (input_date - today_date).days
        
        return delta_days
    
    except ValueError:
        # Обробка помилки неправильного формату дати
        return "Помилка: Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'!"

# 🔹 Приклади виклику функції:
print(get_days_from_today("2025-03-12"))  # Наприклад, -157 (якщо сьогодні 5 травня 2021)
print(get_days_from_today("2027-01-01"))  # Від'ємне число, якщо дата у майбутньому
print(get_days_from_today("lkj=gfd-poi")) # Некоректний формат


#завдання 2
import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує відсортований набір унікальних випадкових чисел для лотерейного квитка.

    :param min: Мінімальне можливе число (не менше 1)
    :param max: Максимальне можливе число (не більше 1000)
    :param quantity: Кількість чисел у наборі
    :return: Відсортований список унікальних випадкових чисел або порожній список, якщо параметри некоректні
    """
    # Перевірка коректності параметрів
    if not (1 <= min <= max <= 1000) or not (min <= quantity <= max):
        return []

    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортуємо числа у порядку зростання
    return sorted(numbers)

# 🔹 Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


 #Завдання 3
import re

def normalize_phone(phone_number):
    """
    Нормалізує номер телефону, залишаючи тільки цифри та знак '+' на початку.
    Якщо номер не має міжнародного коду, додається '+38' (Україна).

    :param phone_number: Рядок з телефонним номером у будь-якому форматі
    :return: Нормалізований телефонний номер
    """

    # Видаляємо всі символи, крім цифр та знака '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    # Перевіряємо формат та додаємо необхідний код
    if cleaned_number.startswith("+"):
        # номер уже має міжнародний код
        return cleaned_number
    elif cleaned_number.startswith("380"):
        # додаємо тільки знак '+'
        return "+" + cleaned_number
    else:
        # додаємо міжнародний код '+38'
        return "+38" + cleaned_number


# 🔹 Приклади використання:
test_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for number in test_numbers:
    normalized = normalize_phone(number)
    print(f"Оригінал: {number}  →  Нормалізований: {normalized}")


#Завдання 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Визначає, кого необхідно привітати з днем народження протягом наступних 7 днів.
    Якщо день народження припадає на вихідні, дата привітання переноситься на понеділок.
    
    Args:
        users (list): Список словників з іменем (name) та датою народження (birthday).

    Returns:
        list: Список словників з іменем та датою привітання.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            if birthday_this_year.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад списку користувачів:
users = [
    {"name": "John Doe", "birthday": "1985.03.14"},
    {"name": "Jane Smith", "birthday": "1990.03.10"},
    {"name": "Emily White", "birthday": "1989.03.14"},
    {"name": "Mike Brown", "birthday": "1988.01.30"}
]

# Використання функції:
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

