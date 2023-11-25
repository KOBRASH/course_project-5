import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host, port):
        # Устанавливаем соединение с базой данных при создании экземпляра класса
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

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