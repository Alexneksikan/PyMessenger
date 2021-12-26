""" 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого
файла!). Затем открыть этот файл и вывести его содержимое на печать. ВАЖНО: файл должен быть открыт без ошибок вне
зависимости от того, в какой кодировке он был создан! """
from chardet import detect

if __name__ == '__main__':

    file_name = 'test_file.txt'

    STR_LIST = ['сетевое программирование', 'сокет', 'декоратор']
    with open(file_name, 'w') as f_n:
        for line in STR_LIST:
            f_n.write(f'{line}\n')

    with open(file_name, 'rb') as f_n:
        content = f_n.read()
    encoding = detect(content)['encoding']
    print(f'Кодировка: {encoding}\n')

    with open(file_name, 'r', encoding=encoding) as f_n:
        for el_str in f_n:
            print(el_str, end="")
