""" 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode). """

if __name__ == '__main__':

    WORD_1 = 'разработка'
    WORD_2 = 'администрирование'
    WORD_3 = 'protocol'
    WORD_4 = 'standard'

    WORDS_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]

    print(f'\nБайтовое представление:')
    bytes_list = []
    for item in WORDS_LIST:
        b_item = item.encode('utf-8')
        print(b_item)
        bytes_list.append(b_item)

    print('-' * 140)

    print(f'\nСтроковое представление:')
    str_list = []
    for item in bytes_list:
        str_item = item.decode('utf-8')
        str_list.append(str_item)

    print(str_list)
