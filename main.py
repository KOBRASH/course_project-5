import requests
import json

def get_employer_id_by_name(employer_name):
    url = f"https://api.hh.ru/employers"
    params = {'text': employer_name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        employers_data = response.json()
        if employers_data.get('items'):
            first_employer = employers_data['items'][0]
            return first_employer['id']
        else:
            return None
    else:
        print(f"Не удалось получить данные для работодателя {employer_name}. Статус код: {response.status_code}")
        return None

def get_vacancies_by_employer_id(employer_name):
    employer_id = get_employer_id_by_name(employer_name)
    if employer_id:
        url = f"https://api.hh.ru/vacancies"
        params = {'employer_id': employer_id}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            vacancies = response.json().get('items', [])
            unique_vacancies = {}  # Используем словарь для хранения уникальных вакансий и их максимальной зарплаты
            for vacancy in vacancies:
                salary = vacancy.get('salary', {})
                if salary and salary.get('to'):
                    vacancy_name = vacancy['name']
                    if vacancy_name not in unique_vacancies or salary['to'] > unique_vacancies[vacancy_name]:
                        unique_vacancies[vacancy_name] = salary['to']
            return {'employer_id': employer_id, 'employer_name': employer_name, 'vacancies': unique_vacancies}
        else:
            print(f"Не удалось получить данные о вакансиях для работодателя {employer_name}. Статус код: {response.status_code}")
    else:
        print(f"Не найден '{employer_name}'")
    return None

employer_names = [
    "ООО ИПО Ю-Питер",
    "ООО Люди Любят",
    "Mail.ru Group",
    "ГКУ ЛО Региональный мониторинговый центр",
    "ООО АТП Невское",
    "Action",
    "Студия Etalon Sport & Dance",
    "Магнит",
    "СП Энергосервис",
    "ООО Правград"
]

all_vacancies_data = {}
for employer_name in employer_names:
    vacancies_data = get_vacancies_by_employer_id(employer_name)
    if vacancies_data:
        all_vacancies_data[employer_name] = vacancies_data

with open('vacancies_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_vacancies_data, json_file, ensure_ascii=False, indent=4)

print("Данные о вакансиях сохранены в файл 'vacancies_data.json'.")
