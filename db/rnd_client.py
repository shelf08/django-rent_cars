import random
import csv



def generate_name(is_female):
    if is_female:
        first_names = ['Анастасия', 'Елена', 'Мария', 'Татьяна', 'Ольга', 'Оксана', 'Валерия', 'Милена', 'Алина']
        last_names = ['Иванова', 'Петрова', 'Сидорова', 'Попова', 'Любимова', 'Лобцова', 'Толстоногова', 'Крохалева']
        middle_names = ['Ивановна', 'Петровна', 'Дмитриевна', 'Алексеевна', 'Михайловна', 'Артемовна', 'Олеговна']
    else:
        first_names = ['Иван', 'Сергей', 'Алексей', 'Дмитрий', 'Николай', 'Георгий', 'Никита', 'Данила']
        last_names = ['Иванов', 'Петров', 'Сидоров', 'Попов', 'Михайлов', 'Лобцов', 'Толстоногов', 'Крохалев']
        middle_names = ['Иванович', 'Петрович', 'Дмитриевич', 'Алексеевич', 'Михайлович', 'Артемович', 'Олегович']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    middle_name = random.choice(middle_names)

    return f"{last_name}_{first_name}_{middle_name}"



def generate_phone_number():
    return '89' + ''.join(random.choices('0123456789', k=9))



def generate_age():
    return random.randint(20, 70)


# Генерация данных
data = []
existing_records = set()

for id in range(0, 1001):
    is_female = random.choice([True, False])
    while True:
        ФИО = generate_name(is_female)
        Номер_телефона = generate_phone_number()
        Возраст = generate_age()

        record = (id, ФИО, Номер_телефона, Возраст)


        if record not in existing_records:
            existing_records.add(record)
            data.append(record)
            break


with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Данные успешно сгенерированы и записаны в файл data.csv.")