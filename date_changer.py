# Запрашиваем информацию у пользователя
username = input("Введите ваше имя (например, Сидорова Маргарита): ")
title = input("Введите заголовок заметки,(например, Список дел: ")
content = input("Введите пункты списка дел, разделяя запятыми (например, купить подарок, записаться на маникюр, заплатить за квартиру): ")
status = input("Статус (введите 'активна' или 'неактивна'): ")
created_date = input("Введите дату создания (в формате ДД-ММ-ГГГГ, например, 10-12-2024): ")
issue_date = input("Введите дату выполнения (в формате ДД-ММ-ГГГГ, например, 20-12-2024): ")

# Выводим введенные данные
print("Имя: ", username)
print("Заголовок заметки: ", title)
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания: ", created_date)
print("Дата выполнения: ", issue_date)
