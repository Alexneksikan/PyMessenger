""" Unit-тесты модуля server.py """
import unittest

from Lesson4.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, \
    RESPONDEFAULT_IP_ADDRESSE
from Lesson4.server import process_client_message


class TestServer(unittest.TestCase):
    """ Класс с тестами сервера """
    err_dict = {
        RESPONDEFAULT_IP_ADDRESSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    def test_ok_check(self):
        """ Тест корректного запроса """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_no_action(self):
        """ Ошибка, если нет действия """
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """ Ошибка, если неизвестное действие """
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """ Ошибка, если запрос не содержит штампа времени """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """ Ошибка, если не указан пользователь """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """ Ошибка - пользователь не Guest """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)

    def test_not_exist_response(self):
        """ Проверка отсутствия параметра RESPONSE при ошибке"""
        self.assertEqual(RESPONSE in process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), False)


if __name__ == '__main__':
    unittest.main()
