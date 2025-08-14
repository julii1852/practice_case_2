from datetime import datetime

# Словарь для дней недели
days_ru = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}

# Словарь цифр для "электронного табло"
digits = {
    "0": [" *** ",
           "*   *",
           "*   *",
           "*   *",
           " *** "],
    "1": ["  *  ",
           " **  ",
           "  *  ",
           "  *  ",
           " *** "],
    "2": [" *** ",
           "*   *",
           "   * ",
           "  *  ",
           "*****"],
    "3": [" *** ",
           "    *",
           " *** ",
           "    *",
           " *** "],
    "4": ["*   *",
           "*   *",
           "*****",
           "    *",
           "    *"],
    "5": ["*****",
           "*    ",
           "**** ",
           "    *",
           "**** "],
    "6": [" *** ",
           "*    ",
           "**** ",
           "*   *",
           " *** "],
    "7": ["*****",
           "    *",
           "   * ",
           "  *  ",
           "  *  "],
    "8": [" *** ",
           "*   *",
           " *** ",
           "*   *",
           " *** "],
    "9": [" *** ",
           "*   *",
           " ****",
           "    *",
           " *** "]
}

def is_leap_year(year):
    """Проверка на високосный год"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_age(birth_date):
    """Вычисление возраста"""
    today = datetime.now()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

if __name__ == "__main__":
    # Запрос данных
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))

    birth_date = datetime(year, month, day)

    # День недели
    day_of_week = days_ru[birth_date.weekday()]

    # Високосный год?
    leap = is_leap_year(year)

    # Возраст
    age = get_age(birth_date)

    # Вывод результатов
    print(f"\nДата рождения: {birth_date.strftime('%d.%m.%Y')}")
    print(f"День недели: {day_of_week}")
    print(f"Високосный год: {'Да' if leap else 'Нет'}")
    print(f"Возраст: {age} лет")

    # Электронное табло
    date_str = f"{day:02}{month:02}{year}"
    print("\nЭлектронное табло:\n")
    for row in range(5):
        for ch in date_str:
            print(digits[ch][row], end="  ")
        print()

    input("\nНажмите Enter, чтобы закрыть программу...")
