import psycopg2
import json

# Подключение к базе данных PostgreSQL (без указания конкретной базы)
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    host="localhost",
    port="5432"
)
conn.autocommit = True  # Устанавливаем режим автокоммита для выполнения запросов

# Проверка существования базы данных "job_vacancies"
cursor = conn.cursor()
cursor.execute("SELECT 1 FROM pg_database WHERE datname='job_vacancies'")
exists = cursor.fetchone()

# Если базы не существует, создаем ее
if not exists:
    try:
        cursor.execute("CREATE DATABASE job_vacancies")
        print("База данных 'job_vacancies' успешно создана")
    except psycopg2.Error as e:
        print("Ошибка при создании базы данных:", e)
else:
    print("База данных 'job_vacancies' уже существует")

cursor.close()
conn.close()

# Подключение к созданной базе данных
conn = psycopg2.connect(
    dbname="job_vacancies",
    user="postgres",
    host="localhost",
    port="5432"
)
conn.autocommit = True  # Устанавливаем режим автокоммита для выполнения запросов

# Создание таблиц employer и vacancies
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employer (
        id SERIAL PRIMARY KEY,
        employer_id TEXT,
        employer_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vacancies (
        id SERIAL PRIMARY KEY,
        employer_id TEXT,
        employer_name TEXT,
        vacancy_name TEXT,
        salary INTEGER
    )
''')

# Чтение данных из файла vacancies_data.json
with open('vacancies_data.json', 'r', encoding='utf-8') as json_file:
    all_vacancies_data = json.load(json_file)

# Заполнение таблиц данными из vacancies_data.json
for employer_name, data in all_vacancies_data.items():
    employer_id = data['employer_id']
    employer_name = data['employer_name']

    # Добавление записи в таблицу employer
    cursor.execute('''
        INSERT INTO employer (employer_id, employer_name)
        VALUES (%s, %s)
    ''', (employer_id, employer_name))

    # Добавление записей в таблицу vacancies
    for vacancy_name, salary in data['vacancies'].items():
        cursor.execute('''
            INSERT INTO vacancies (employer_id, employer_name, vacancy_name, salary)
            VALUES (%s, %s, %s, %s)
        ''', (employer_id, employer_name, vacancy_name, salary))

cursor.close()
conn.close()

print("База данных и таблицы успешно созданы и заполнены данными из 'vacancies_data.json'.")
