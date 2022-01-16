import json
import unittest
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from Lesson4.common.utils import send_message, get_message
from Lesson4.common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, ENCODING


class TestUtils(unittest.TestCase):
    """ Тестовый класс для проверки """
    test_message = {
        'action': 'presence',
        'time': 1,
        'type': 'status',
        'user': {
            'account_name': 'User',
            'password': ''
        }
    }
    test_correct_response = {
        'response': 200,
        'time': 1,
        'alert': 'Соединение прошло успешно'
    }
    test_error_response = {
        'response': 400,
        'time': 1,
        'error': 'Ошибка соединения'
    }

    server_socket = None
    client_socket = None

    def setUp(self) -> None:
        # Тестовый сокет для сервера
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.server_socket.listen(MAX_CONNECTIONS)
        # Тестовый сокет для клиента
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.client, self.client_address = self.server_socket.accept()

    def tearDown(self) -> None:
        # Закрытие сокетов
        self.client.close()
        self.client_socket.close()
        self.server_socket.close()

    def test_send_wrong_message_from_client(self):
        # Проверка исключения, если на входе не словарь
        self.assertRaises(TypeError, send_message, self.client_socket, 'not dictionary')

    def test_send_correct_message_from_client(self):
        # Проверка отправки корректного сообщения
        send_message(self.client_socket, self.test_message)
        test_response = self.client.recv(MAX_PACKAGE_LENGTH)
        test_response = json.loads(test_response.decode(ENCODING))
        self.client.close()
        self.assertEqual(self.test_message, test_response)

    def test_get_message_200(self):
        # Корректная расшифровка корректного словаря
        message = json.dumps(self.test_correct_response)
        self.client.send(message.encode(ENCODING))
        self.client.close()
        response = get_message(self.client_socket)
        self.assertEqual(self.test_correct_response, response)

    def test_get_message_400(self):
        # Отработка ошибки расшифровки неправильного словаря
        message = json.dumps(self.test_error_response)
        self.client.send(message.encode(ENCODING))
        self.client.close()
        response = get_message(self.client_socket)
        self.assertEqual(self.test_error_response, response)


if __name__ == '__main__':
    unittest.main()
