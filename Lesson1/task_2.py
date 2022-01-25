""" 2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
encode и decode) и определить тип, содержимое и длину соответствующих переменных. """


def str_info(items: list):
    for item in items:
        b_item = eval(f"b'{item}'")
        print(f'{b_item}: тип {type(b_item)}, длина {len(b_item)} байтов')
    print('-' * 50)


if __name__ == '__main__':
    STR_1 = 'class'
    STR_2 = 'function'
    STR_3 = 'method'

    example = [STR_1, STR_2, STR_3]
    str_info(example)
