# Запрашиваем у пользователя информацию для создания заметки
username = input("Введите ваше Имя: ")
content = input("Описание заметки: ")
status = input("Статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


# Создаем список заголовков заметки
titles = []
for i in range(5):
    title = input(f"Заголовок заметки {i + 1}: ")
    titles.append(title)
# Выводим все данные заметки
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)

