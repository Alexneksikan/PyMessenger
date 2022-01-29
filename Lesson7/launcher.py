"""Лаунчер"""

from subprocess import Popen, CREATE_NEW_CONSOLE

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(Popen('python server.py', creationflags=CREATE_NEW_CONSOLE))
        for i in range(2):
            PROCESS.append(Popen('python client.py -m send', creationflags=CREATE_NEW_CONSOLE))
        for i in range(5):
            PROCESS.append(Popen('python client.py -m listen', creationflags=CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
