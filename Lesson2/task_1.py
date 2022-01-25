""" 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. """
import csv
import re
from pprint import pprint

import numpy as np
from chardet import detect

if __name__ == '__main__':

    def get_data():

        info_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
        os_prod_list = []
        os_name_list = []
        os_code_list = []
        os_type_list = []
        main_data = []

        for item in info_files:
            with open(item, 'rb') as f_n:
                content = f_n.read()
            encoding = detect(content)['encoding']
            data = content.decode(encoding)
            f_n.close()

            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

            os_name_reg = re.compile(r'Windows\s\S*')
            os_name_list.append(os_name_reg.findall(data)[0])

            os_code_reg = re.compile(r'Код продукта:\s*\S*')
            os_code_list.append(os_code_reg.findall(data)[0].split()[2])

            os_type_reg = re.compile(r'Тип системы:\s*\S*')
            os_type_list.append(os_type_reg.findall(data)[0].split()[2])

        headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
        main_data.append(headers)
        trans_data = np.array([os_prod_list, os_name_list, os_code_list, os_type_list]).transpose()
        main_data = np.concatenate((main_data, trans_data)).tolist()

        return main_data


    def write_to_csv(res_file):

        main_data = get_data()
        with open(res_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for row in main_data:
                writer.writerow(row)
        file.close()


    write_to_csv('data_report.csv')
