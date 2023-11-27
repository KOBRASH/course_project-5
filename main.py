from db_manager import DBManager

def main():
    # Инициализация объекта DBManager для работы с базой данных
    db_manager = DBManager(
        dbname='your_dbname',
        user='your_user',
        password='your_password',
        host='your_host',
        port='your_port'
    )

    while True:
        print("Меню:")
        print("1. Получить список всех компаний и количество вакансий")
        print("2. Получить список всех вакансий")
        print("3. Получить среднюю зарплату по вакансиям")
        print("4. Получить список вакансий с зарплатой выше средней")
        print("5. Получить список вакансий по ключевому слову")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            companies_vacancies_count = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний и количество вакансий:")
            print(companies_vacancies_count)
        elif choice == "2":
            all_vacancies = db_manager.get_all_vacancies()
            print("Список всех вакансий:")
            print(all_vacancies)
        elif choice == "3":
            avg_salary = db_manager.get_avg_salary()
            print("Средняя зарплата по вакансиям:")
            print(avg_salary)
        elif choice == "4":
            vacancies_higher_salary = db_manager.get_vacancies_with_higher_salary()
            print("Список вакансий с зарплатой выше средней:")
            print(vacancies_higher_salary)
        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
            print(f"Список вакансий с ключевым словом '{keyword}':")
            print(vacancies_with_keyword)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующую опцию.")

    # Закрытие соединения с базой данных после работы
    db_manager.close_connection()

if __name__ == "__main__":
    main()
