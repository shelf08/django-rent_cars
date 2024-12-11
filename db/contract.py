import sqlite3
import csv
import random
from datetime import datetime, timedelta

# # Имя выходного файла
# filename = 'contract.csv'
#
# # Начальная дата для договора
# start_date = datetime(2023, 1, 1)
#
# # Создаем 1000 строк для таблицы Договор_аренды
# with open(filename, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Код_договора', 'Стоимость_аренды', 'Дата', 'Время_начала', 'Время_окончания', 'id_автомобиля',
#                      'id_клиента'])
#     for i in range(1, 1001):
#         код_договора = i
#         дата = start_date.strftime('%Y-%m-%d')  # Формат даты
#         время_начала = f"{random.randint(0, 23):02}:{random.choice([0, 30]):02}"
#         # Генерируем продолжительность (от 30 минут до 2 часов)
#         продолжительность = random.choice([30, 60, 90, 120])
#         # Вычисляем время окончания
#         время_начала_dt = datetime.strptime(f"{дата} {время_начала}", '%Y-%m-%d %H:%M')
#         время_окончания_dt = время_начала_dt + timedelta(minutes=продолжительность)
#         время_окончания = время_окончания_dt.strftime('%H:%M')
#
#
#         стоимость_аренды = (продолжительность // 30) * 500
#
#         id_автомобиля = random.randint(1, 12)
#         id_клиента = код_договора
#
#         writer.writerow([код_договора, стоимость_аренды, дата, время_начала, время_окончания, id_автомобиля, id_клиента])
#
# print(f"Файл {filename} успешно создан!")


"""""""""""""""""""""""""""""""""//"""""""""""""""""""""""""""""""""


conn = sqlite3.connect('database1.db')
cursor = conn.cursor()


with open('contract.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute('INSERT INTO Договор_аренды (Код_договора, Стоимость_аренды, Дата, Время_начала, Время_окончания, id_автомобиля, id_клиента) VALUES (?, ?, ?, ?, ?, ?, ?)', row)


conn.commit()
conn.close()

print("Данные успешно загружены в базу данных!")