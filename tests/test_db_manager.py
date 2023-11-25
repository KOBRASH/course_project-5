import unittest
from db_manager import DBManager

# Тестирование класса DBManager
class TestDBManager(unittest.TestCase):
    def setUp(self):
        # Подготовка объекта DBManager для тестов
        self.db_manager = DBManager(
            dbname='your_dbname',
            user='your_user',
            password='your_password',
            host='your_host',
            port='your_port'
        )

    def test_get_companies_and_vacancies_count(self):
        # Тест метода get_companies_and_vacancies_count
        # Получаем данные о компаниях и их вакансиях
        result = self.db_manager.get_companies_and_vacancies_count()
        # Проверяем, что результат не пустой
        self.assertIsNotNone(result)
        # Проверяем тип данных результата
        self.assertIsInstance(result, list)
        # Проверяем, что данные содержат пары компания-количество вакансий
        for row in result:
            self.assertIsInstance(row, tuple)
            self.assertEqual(len(row), 2)
            self.assertIsInstance(row[0], str)
            self.assertIsInstance(row[1], int)

    def test_get_all_vacancies(self):
        # Тест метода get_all_vacancies
        # Получаем все вакансии
        result = self.db_manager.get_all_vacancies()
        # Проверяем, что результат не пустой
        self.assertIsNotNone(result)
        # Проверяем тип данных результата
        self.assertIsInstance(result, list)
        # Проверяем, что данные содержат информацию о вакансиях
        for row in result:
            self.assertIsInstance(row, tuple)
            self.assertEqual(len(row), 4)
            self.assertIsInstance(row[0], str)
            self.assertIsInstance(row[1], str)
            self.assertIsInstance(row[2], (int, float))
            self.assertIsInstance(row[3], str)

    # Добавьте тесты для других методов

    def tearDown(self):
        # Закрываем соединение после выполнения тестов
        self.db_manager.close_connection()

if __name__ == '__main__':
    unittest.main()
