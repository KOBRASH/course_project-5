import unittest
from unittest.mock import MagicMock
from hh_api import HHAPIClient


class TestHHAPIClient(unittest.TestCase):
    def setUp(self):
        # Создаем mock-объект для requests
        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {'items': [{'id': '123'}]}

        self.mock_requests = MagicMock()
        self.mock_requests.get.return_value = self.mock_response

        self.hh_client = HHAPIClient(token='test_token')
        self.hh_client.requests = self.mock_requests  # Подменяем requests на mock-объект

    def test_get_company_data_success(self):
        # Тест метода get_company_data при успешном запросе
        company_name = 'Тестовая компания'
        company_data = self.hh_client.get_company_data(company_name)

        self.mock_requests.get.assert_called_once()
        self.assertEqual(company_data[0]['id'], '123')

    def test_get_vacancies_by_company_success(self):
        # Тест метода get_vacancies_by_company при успешном запросе
        vacancies = self.hh_client.get_vacancies_by_company('123')

        self.mock_requests.get.assert_called_once()
        self.assertTrue(len(vacancies) > 0)

    def test_get_company_data_failure(self):
        # Тест метода get_company_data при ошибке запроса
        self.mock_response.status_code = 404  # Устанавливаем код ошибки

        company_name = 'Неизвестная компания'
        company_data = self.hh_client.get_company_data(company_name)

        self.mock_requests.get.assert_called_once()
        self.assertEqual(len(company_data), 0)


if __name__ == '__main__':
    unittest.main()
