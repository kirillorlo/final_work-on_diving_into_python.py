#Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
#Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

# import json


# def txt_to_json(source, output):
#     data1 = {}
#     with open(source, 'r') as f:
#         data = f.read()

#     for line in data.split('\n'):
#         name, number = line.split(' ')
#         data1[name.capitalize()] = float(number)


#     with open(output, 'w') as f:
#         json.dump(data1, f, indent=4)



# if __name__ == '__main__':
#     txt_to_json('data.txt', 'output.json')

#Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.

# import json
# import os

# #{level: {id: name}}


# def load_or_create(file_name: str):
#     if file_name in os.listdir():
#         with open(file_name, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#             return data

#     with open(file_name, 'w') as f:
#         json.dump({}, f)
#     return {}


# def enter_users(level: str, id: str, name: str, file_name: str) -> None:
#     data = load_or_create(file_name)
#     for value in data.values():
#         if id in value:
#             raise ValueError("id уже существует")

#     data.setdefault(level, {})
#     data[level].setdefault(id, name)

#     with open(file_name, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4)
#     return


# if __name__ == '__main__':
#     enter_users('5', '12345656', 'Alex', 'data1.json')

# Напишите функцию, которая сохраняет созданный
# в прошлом задании файл в формате CSV.
import csv
import json


def json_to_csv(json_in: str, csv_out: str) -> None:
    with (
        open(json_in, 'r', newline='', encoding='utf-8') as f_in,
        open(csv_out, 'w', newline='', encoding='utf-8') as f_out,
    ):
        data = json.load(f_in)
        all_data = []
        csv_write = csv.DictWriter(f_out, fieldnames=['level', 'id', 'name'])
        for level, inner_dict in data.items():
            for id_, name in inner_dict.items():
                all_data.append({"id": id_, "level": level, "name": name})
        csv_write.writeheader()
        csv_write.writerows(all_data)


if __name__ == '__main__':
    json_to_csv('task02.json', 'task02.csv')
