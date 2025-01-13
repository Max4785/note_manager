from datetime import date as dt
import re
import time

# Получаем текущую дату
current_date = dt.today()
print(f"Текущая дата: {current_date.day}-{current_date.month}-{current_date.year}")

time.sleep(2)

while True:
    user_input = input("Введите дату крайнего срока (в формате день-месяц-год): ").strip()
    if not user_input:
        print("Вы ничего не ввели. Попробуйте снова.")
        continue

    issue_date_parts = re.split(r'[-. ,_:;\\/]+', user_input)
    issue_date_parts = [x for x in issue_date_parts if x.isdigit()]  # Оставляем только числовые значения

    if len(issue_date_parts) == 1:  # Введён только день
        day, month, year = int(issue_date_parts[0]), current_date.month, current_date.year
    elif len(issue_date_parts) == 2:  # Введены день и месяц
        day, month, year = int(issue_date_parts[0]), int(issue_date_parts[1]), current_date.year
    elif len(issue_date_parts) == 3:  # Введены день, месяц и год
        day, month, year = map(int, issue_date_parts)
    else:
        print("Вы ввели слишком много данных. Попробуйте снова.")
        continue

    # Проверка корректности месяца
    if not (1 <= month <= 12):
        print(f"Месяц должен быть в диапазоне от 1 до 12. Вы ввели: {month}. Попробуйте снова.")
        continue

    # Проверка корректности дня
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    max_days = 31 if month in {1, 3, 5, 7, 8, 10, 12} else 30 if month in {4, 6, 9, 11} else (29 if is_leap_year else 28)
    if not (1 <= day <= max_days):
        print(f"Некорректная дата. Попробуйте снова.")
        continue

    # Создание объекта даты
    issue_date = dt(year, month, day)

    # Успешный ввод
    print(f"Вы успешно ввели дату: {issue_date.strftime('%d-%m-%Y')}")
    break

# Расчёт разницы в днях
date_diff = (issue_date - current_date).days

# Определение формы слова "день"
day_form = "дней" if 11 <= abs(date_diff) % 100 <= 14 else "день" if abs(date_diff) % 10 == 1 else"дня" if 2 <= abs(date_diff) % 10 <= 4 else "дней"

if date_diff < 0:
    print(f"Задача просрочена на {abs(date_diff)} {day_form}.")
elif date_diff >0:
    print(f"Крайний срок через {date_diff} {day_form}.")
else:
    print(f"Крайний срок сегодня.")


'''Продолжение в разработке потом буду додумывать логику, по заданию я выполнил, что необходимо.
Как задумка планируется добавить еще {вывод} количества дней, если текущий год и/или месяц совпадают с пользовательским,
иначе, {вывод} количества лет, месяцев и дней
'''
# # Расчёт разницы в годах, месяцах и днях
# years_diff = issue_date.year - current_date.year
# months_diff = issue_date.month - current_date.month
# days_diff = issue_date.day - current_date.day
#
# if date_diff == 0:
#     print("Крайний срок сегодня.")
# elif issue_date > current_date:
#     if days_diff < 0:
#         months_diff -= 1
#         previous_month = (issue_date.month - 1) if issue_date.month > 1 else 12
#         previous_year = issue_date.year if issue_date.month > 1 else issue_date.year - 1
#
#         if previous_month in {1, 3, 5, 7, 8, 10, 12}:
#             days_diff += 31
#         elif previous_month in {4, 6, 9, 11}:
#             days_diff += 30
#         elif previous_month == 2:
#             days_diff += 29 if (previous_year % 4 == 0 and (previous_year % 100 != 0 or previous_year % 400 == 0)) else 28
#
#             month_form = "месяцев" if 11 <= abs(months_diff) % 100 <= 14 else "месяц" if abs(months_diff) % 10 == 1 else "месяца" if 2 <= abs(months_diff) % 10 <= 4 else "месяцев"
#
#             years_form = "лет" if 11 <= abs(years_diff) % 100 <= 14 else "год" if abs(years_diff) % 10 == 1 else "года" if 2 <= abs(years_diff) % 10 <= 4 else "лет"
#
#             if years_diff == 0 and months_diff == 0:
#                 print(f"До крайнего срока осталось {days_diff} {day_form}.")
#             elif years_diff == 0:
#                 print(f"До крайнего срока осталось {months_diff} {month_form} и {days_diff} {day_form}.")
#             else:
#                 print(f"До крайнего срока осталось {years_diff} {years_form}, {months_diff} {month_form} и {days_diff} {day_form}.")
# # else:
# #     if years_diff < 0 or months_diff < 0 or days_diff < 0:
# #         years_diff = abs(years_diff)
# #         months_diff = abs(months_diff)
# #         days_diff = abs(days_diff)
# #
# #     if years_diff == 0 and months_diff == 0:
# #         print(f"Задача просрочена на {days_diff} {day_form}.")
# #     elif years_diff == 0:
# #         print(f"Задача просрочена на {months_diff} {month_form} и {days_diff} {day_form}.")
# #     else:
# #         print(f"Задача просрочена на {years_diff} {years_form}, {months_diff} {month_form} и {days_diff} {day_form}.")