username = str(input("Введите ваше имя: "))
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки(пример-в работе): ")
created_date = input('Введите дату создания заметки в числовом формате(например: 01-01-2025): ')
issue_date = input('Введите дату истечения заметки в числовом формате(например: 11-01-2025): ')

temp_created_date = created_date[0:2] + "." + created_date[3:5] # Переменная хранящая данные дня и месяца в виде дд.мм
temp_issue_date = issue_date[0:2] + "." + issue_date[3:5]

print(f"Пользователь: {username}",
      f"Заголовок: {title} ({status}) \n{temp_created_date}-{temp_issue_date}",
      f"Описание: {content}",
      f"Дата создания заметки: {created_date[0:2]}.{created_date[3:5]}.{created_date[6:]}",# Выводится день-месяц
      f"Дата истечения заметки: {issue_date[0:2]}.{issue_date[3:5]}.{issue_date[6:]}",
      sep='\n')
