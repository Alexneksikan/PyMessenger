""" 3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе. Для проверки
правильности работы кода используйте значения: «attribute», «класс», «функция», «type» """

if __name__ == '__main__':

    WORD_1 = 'attribute'
    WORD_2 = 'класс'
    WORD_3 = 'функция'
    WORD_4 = 'type'

    WORDS_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]

    for item in WORDS_LIST:
        try:
            item.encode('ascii')
        except UnicodeEncodeError:
            print(f'Слово "{item}" невозможно записать в байтовом типе.')
