title = []

username = str(input("Введите ваше имя: "))

title_0 = input("Введите первый заголовок заметки: ")
title.append(title_0)
title_1 = input("Введите второй заголовок заметки: ")
title.append(title_1)
title_2 = input("Введите третий заголовок заметки: ")
title.append(title_2)

content = input("Введите описание заметки: ")
status = input("Введите статус заметки(пример-в работе): ")

created_date = input('Введите дату создания заметки в числовом формате(например: 01-01-2025): ')
issue_date = input('Введите дату истечения заметки в числовом формате(например: 11-01-2025): ')

temp_created_date = created_date[0:2] + "." + created_date[3:5] # Переменная хранящая данные дня и месяца в виде дд.мм
temp_issue_date = issue_date[0:2] + "." + issue_date[3:5]

print(f"Пользователь: {username}",
      f"Заголовки: 1.{title[0]} 2.{title[1]} 3.{title[2]}",
      f"Описание: {content}",
      f"Статус заявки: {status}",
      f"Диапазон: {temp_created_date}-{temp_issue_date}",
      # После заголовков сделал диапазон выполнения по времени задачи для наглядности
      f"Дата создания заметки: {created_date[0:2]}.{created_date[3:5]}.{created_date[6:]}",# Выводится день-месяц
      f"Дата истечения заметки: {issue_date[0:2]}.{issue_date[3:5]}.{issue_date[6:]}",
      sep='\n')
