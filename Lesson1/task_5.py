""" 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтового в строковый (
предварительно определив кодировку выводимых сообщений). """
import platform
import subprocess
from chardet import detect

if __name__ == '__main__':

    urls = ['yandex.ru', 'youtube.com']
    q_pings = '4'
    code = '-n' if platform.system().lower() == 'windows' else '-c'

    for url in urls:
        args = ['ping', code, q_pings, url]
        subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

        for line in subproc_ping.stdout:
            enc = detect(line)
            line = line.decode(enc['encoding']).encode('utf-8')
            print(line.decode('utf-8'), end="")
