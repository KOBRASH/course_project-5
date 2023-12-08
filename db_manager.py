import psycopg2
from psycopg2 import sql

class DBManager:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        self.cursor.execute('''
            SELECT employer_name, COUNT(*) as vacancies_count
            FROM vacancies
            GROUP BY employer_name
        ''')
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        self.cursor.execute('''
            SELECT employer_name, vacancy_name, salary
            FROM vacancies
        ''')
        return self.cursor.fetchall()

    def get_avg_salary(self):
        self.cursor.execute('''
            SELECT AVG(salary) as average_salary
            FROM vacancies
        ''')
        return self.cursor.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        self.cursor.execute('''
            SELECT employer_name, vacancy_name, salary
            FROM vacancies
            WHERE salary > %s
        ''', (avg_salary,))
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        self.cursor.execute(sql.SQL('''
            SELECT employer_name, vacancy_name, salary
            FROM vacancies
            WHERE vacancy_name ILIKE %s
        '''), (f'%{keyword}%',))
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
