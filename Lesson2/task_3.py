""" 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. """
import yaml

if __name__ == '__main__':

    data_in = {'items': ['складные', 'дорожные', 'детские'],
               'quantity': 3,
               'prices': {'складные': '15\u0023',
                          'дорожные': '7\u0023',
                          'детские': '10\u0023'}
               }

    with open('file.yaml', 'w', encoding='utf-8') as f_in:
        yaml.dump(data_in, f_in, default_flow_style=False, allow_unicode=True)

    with open('file.yaml', 'r', encoding='utf-8') as f_out:
        data_out = yaml.load(f_out, Loader=yaml.SafeLoader)

    print(data_in == data_out)
