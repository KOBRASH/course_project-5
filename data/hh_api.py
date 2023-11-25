import requests

class HHAPIClient:
    def __init__(self, token):
        self.base_url = 'https://api.hh.ru/'
        self.headers = {'Authorization': f'Bearer {token}'}

    def get_vacancies_by_company(self, company_id):
        # Метод для получения списка вакансий по ID компании
        url = f'{self.base_url}vacancies'
        params = {'employer_id': company_id}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            vacancies = response.json()
            return vacancies['items']
        else:
            print(f'Ошибка при запросе вакансий компании {company_id}: {response.status_code}')
            return []

    def get_company_data(self, company_name):
        # Метод для получения данных о компании по ее названию
        url = f'{self.base_url}employers'
        params = {'text': company_name}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            companies = response.json()
            return companies['items']
        else:
            print(f'Ошибка при запросе данных о компании {company_name}: {response.status_code}')
            return []

# Пример использования класса HHAPIClient
if __name__ == '__main__':
    # Замените 'YOUR_TOKEN' на ваш токен для доступа к API HH.ru
    hh_client = HHAPIClient(token='YOUR_TOKEN')

    # Получение данных о компании по названию
    company_name = 'Название компании'
    company_data = hh_client.get_company_data(company_name)
    if company_data:
        company_id = company_data[0]['id']
        print(f'ID компании "{company_name}": {company_id}')

        # Получение вакансий компании по ее ID
        vacancies = hh_client.get_vacancies_by_company(company_id)
        if vacancies:
            print(f'Вакансии компании "{company_name}":')
            for vacancy in vacancies:
                print(f'Название: {vacancy["name"]}, Зарплата: {vacancy["salary"]}')

    # Пример обработки ошибок или пустых результатов
    else:
        print(f'Компания "{company_name}" не найдена или произошла ошибка при получении данных.')
