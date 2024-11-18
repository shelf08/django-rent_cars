import sqlite3
import csv

# filename = 'club_cards.csv'
#
#
# with open(filename, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['id', 'Количество бонусов', 'id_клиента'])
#     for i in range(1, 1001):
#         id_клиента = i
#         количество_бонусов = 0
#         writer.writerow([i, количество_бонусов, id_клиента])
#
# print(f"Файл {filename} успешно создан!")

"""""""""""""""""""""""//"""""""""""""""""""""""""""

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


with open('club_cards.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute('INSERT INTO Клубная_карта (id, Количество_бонусов, id_клиента) VALUES (?, ?, ?)', row)

conn.commit()
conn.close()

print("Данные успешно загружены в базу данных!")