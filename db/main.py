import sqlite3
import pandas as pd

# Шаг 1: Загрузка данных из CSV файла
csv_file = 'contract.csv'
data = pd.read_csv(csv_file)

# Шаг 2: Подключение к SQLite базе данных
conn = sqlite3.connect('database2.db')  # Замените на имя вашей базы данных
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Contract (
    contract VARCHAR(100) NOT NULL,
    cost DECIMAL NOT NULL,
    date DATE NOT NULL,
    time_start TIME NOT NULL,
    time_finish TIME NOT NULL,
    automobile BIGINT NOT NULL,
    client BIGINT NOT NULL,
)
''')
# Шаг 4: Вставка данных в таблицу
data.to_sql('Contract', conn, if_exists='append', index=False)

# Шаг 5: Закрытие подключения
conn.commit()
conn.close()