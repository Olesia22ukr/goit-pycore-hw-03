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
print(get_days_from_today("2025-03-10"))  # Наприклад, -157 (якщо сьогодні 5 травня 2021)
print(get_days_from_today("2027-01-01"))  # Від'ємне число, якщо дата у майбутньому
print(get_days_from_today("lkj=gfd-poi")) # Некоректний формат