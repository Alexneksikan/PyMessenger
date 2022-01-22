""" 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. """
import json

if __name__ == '__main__':

    def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str):

        with open('orders.json', 'r', encoding='utf-8') as f_out:
            data = json.load(f_out)

        with open('orders.json', 'w', encoding='utf-8') as f_in:
            orders_list = data['orders']
            order_info = {
                'item': item,
                'quantity': quantity,
                'price': price,
                'buyer': buyer,
                'date': date
            }
            orders_list.append(order_info)
            json.dump(data, f_in, indent=4, ensure_ascii=False)


    write_order_to_json('Roadkiller', '1', '40000', 'Иванов А.А.', '12.10.1998')
    write_order_to_json('Lentus', '4', '55000', 'Gordon Freeman', '31.12.2021')
    write_order_to_json('Krabi', '2', '32000', 'G-Man', '07.11.1974')
