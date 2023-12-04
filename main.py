from db_manager import DBManager

def main():
    db_manager = DBManager()

    while True:
        print("\nМеню:")
        print("1. Добавить компанию")
        print("2. Добавить вакансию")
        print("3. Получить список всех компаний и количество вакансий у каждой")
        print("4. Получить список всех вакансий")
        print("5. Получить среднюю зарплату по вакансиям")
        print("6. Получить список вакансий с зарплатой выше средней")
        print("7. Получить список вакансий по ключевому слову")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            company_name = input("Введите название компании: ")
            db_manager.insert_company_data(company_name)
            print("Компания добавлена успешно.")
        elif choice == "2":
            company_id = int(input("Введите ID компании: "))
            title = input("Введите название вакансии: ")
            salary = float(input("Введите зарплату: "))
            link = input("Введите ссылку на вакансию: ")
            db_manager.insert_vacancy_data(company_id, title, salary, link)
            print("Вакансия добавлена успешно.")
        elif choice == "3":
            companies_vacancies_count = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний и количество вакансий:")
            print(companies_vacancies_count)
        elif choice == "4":
            all_vacancies = db_manager.get_all_vacancies()
            print("Список всех вакансий:")
            print(all_vacancies)
        elif choice == "5":
            avg_salary = db_manager.get_avg_salary()
            print("Средняя зарплата по вакансиям:")
            print(avg_salary)
        elif choice == "6":
            vacancies_higher_salary = db_manager.get_vacancies_with_higher_salary()
            print("Список вакансий с зарплатой выше средней:")
            print(vacancies_higher_salary)
        elif choice == "7":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
            print(f"Список вакансий с ключевым словом '{keyword}':")
            print(vacancies_with_keyword)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующую опцию.")

    db_manager.close_connection()

if __name__ == "__main__":
    main()
