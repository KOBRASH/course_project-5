import psycopg2
from config import DB_CONFIG

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()
        self.create_tables()  # Вызываем метод для создания таблиц при инициализации

    def create_tables(self):
        """Метод для создания таблиц в базе данных"""
        create_companies_table = """
            CREATE TABLE IF NOT EXISTS companies (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
        """

        create_vacancies_table = """
            CREATE TABLE IF NOT EXISTS vacancies (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id),
                title TEXT NOT NULL,
                salary NUMERIC,
                link TEXT
            );
        """

        # Создание таблиц
        self.cur.execute(create_companies_table)
        self.cur.execute(create_vacancies_table)
        self.conn.commit()


    def get_companies_and_vacancies_count(self):
        # Метод для получения списка компаний и количества вакансий у каждой компании
        self.cur.execute("SELECT company_name, COUNT(*) FROM vacancies GROUP BY company_name;")
        return self.cur.fetchall()

    def get_all_vacancies(self):
        # Метод для получения всех вакансий с указанием компании, названия вакансии, зарплаты и ссылки
        self.cur.execute("SELECT company_name, vacancy_title, salary, vacancy_link FROM vacancies;")
        return self.cur.fetchall()

    def get_avg_salary(self):
        # Метод для получения средней зарплаты по всем вакансиям
        self.cur.execute("SELECT AVG(salary) FROM vacancies;")
        return self.cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        # Метод для получения вакансий с зарплатой выше средней по всем вакансиям
        avg_salary = self.get_avg_salary()
        self.cur.execute("SELECT company_name, vacancy_title, salary, vacancy_link FROM vacancies WHERE salary > %s;", (avg_salary,))
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        # Метод для получения вакансий, в названии которых есть ключевое слово
        self.cur.execute("SELECT company_name, vacancy_title, salary, vacancy_link FROM vacancies WHERE vacancy_title ILIKE %s;", ('%' + keyword + '%',))
        return self.cur.fetchall()

    def close_connection(self):
        # Метод для закрытия соединения с базой данных
        self.cur.close()
        self.conn.close()
