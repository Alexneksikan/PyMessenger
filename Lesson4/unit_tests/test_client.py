""" Unit-тесты модуля client.py """
import unittest

from Lesson4.client import create_presence, process_ans
from Lesson4.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE


class TestClient(unittest.TestCase):
    """ Класс с тестами клиента"""
    def test_def_presence(self):
        """ Тест корректного запроса """
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """ Тест корректного разбора ответа 200 """
        self.assertEqual(process_ans({RESPONSE: 200}), '200: OK')

    def test_400_ans(self):
        """ Тест корректного разбора ответа 400 """
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """ Тест исключения без поля RESPONSE """
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

    def test_name_user(self):
        """ Тест корректного имени пользователя """
        self.assertEqual(create_presence('User123')[USER][ACCOUNT_NAME], 'User123')

    def test_time_presence(self):
        """ Проверка корректности параметра TIME """
        self.assertGreater(create_presence()[TIME], 1642352253.1613634)


if __name__ == '__main__':
    unittest.main()
