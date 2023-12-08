from db_manager import DBManager
import subprocess

# Запуск main.py
subprocess.run(["/usr/bin/python3", "main.py"])

# Запуск create_database_tables.py
subprocess.run(["/usr/bin/python3", "create_database_tables.py"])

# Запуск menu.py
subprocess.run(["/usr/bin/python3", "menu.py"])


def print_menu():
    print("Выберите действие:")
    print("1. Получить список всех компаний и количество их вакансий")
    print("2. Получить список всех вакансий")
    print("3. Получить среднюю зарплату по вакансиям")
    print("4. Получить список вакансий с зарплатой выше средней")
    print("5. Получить список вакансий с ключевым словом")
    print("0. Выйти")

def main():
    db_manager = DBManager("job_vacancies", "postgres", "password")  # Замените "password" на ваше реальное значение пароля
    choice = None

    while choice != '0':
        print_menu()
        choice = input("Введите номер действия: ")

        if choice == '1':
            companies_with_vacancies = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний и количество их вакансий:")
            for company in companies_with_vacancies:
                print(f"{company[0]}: {company[1]} вакансий")

        elif choice == '2':
            all_vacancies = db_manager.get_all_vacancies()
            print("Список всех вакансий:")
            for vacancy in all_vacancies:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}")

        elif choice == '3':
            avg_salary = db_manager.get_avg_salary()
            print(f"Средняя зарплата по вакансиям: {avg_salary}")

        elif choice == '4':
            vacancies_above_avg_salary = db_manager.get_vacancies_with_higher_salary()
            print("Список вакансий с зарплатой выше средней:")
            for vacancy in vacancies_above_avg_salary:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}")

        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
            print(f"Список вакансий с ключевым словом '{keyword}':")
            for vacancy in vacancies_with_keyword:
                print(f"Компания: {vacancy[0]}, Вакансия: {vacancy[1]}, Зарплата: {vacancy[2]}")

        elif choice == '0':
            print("Выход")

        else:
            print("Пожалуйста, выберите корректный номер действия.")

    db_manager.close_connection()

if __name__ == "__main__":
    main()
