# Создаем пустой список для хранения заголовков
titles = []

# Запускаем бесконечный цикл, чтобы пользователь мог вводить заголовки
while True:
    # Запрашиваем у пользователя ввод заголовка, добавил функцию .strip(), чтоб удалить начальные и конечные пробелы
    title = input("Введите заголовок (если хотите завершить ввод, оставьте строку пустой или напишите \"стоп\"): ").strip()

    # Проверяем, если пользователь оставил строку пустой (для завершения ввода)
    if title == "":
        break  # Завершаем цикл, если пользователь не ввел заголовок

    # Проверяем, если пользователь ввел команду "стоп" для завершения ввода
    if title.lower() == "стоп":
        break  # Завершаем цикл, если пользователь ввел команду "стоп"

    # Если в списке нет введенного заголовка, добавляем его в список, иначе выводим, что заголовок уже существует
    if title not in titles:
        titles.append(title)
    else:
        print(f"Заголовок '{title}' уже существует. Введите другой.")

# Выводим заголовки пользователю используя индексацию и бесконечный цикл, чтоб вывелись все элементы списка с индексом
print("Заголовки заметки: ")
index = 1
while index <= len(titles):
    print(f"{index}. {titles[index - 1]}")
    index = index + 1
"""
Можно без индекса, тогда:
tit = 0
while tit < len(titles):
    print(f"- {titles[tit - 1]}")
    tit = tit + 1
"""
