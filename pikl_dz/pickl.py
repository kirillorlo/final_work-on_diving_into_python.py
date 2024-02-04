# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
# import json
# import os
# import pickle


# def save_json_to_pickle(path_in: str):
#     ext = '.json'

#     os.chdir(path_in)
#     for file in os.listdir():
#         if not file.endswith(ext):
#             continue
#         pickle_out, _ = file.split('.')
#         with (
#             open(file, 'r') as f_in,
#             open(f'{pickle_out}.pickle', 'wb') as f_out,
#         ):
#             pickle.dump(json.load(f_in), f_out)


# if __name__ == '__main__':
#     save_json_to_pickle(r'E:\Coding\Projects\GB_Python_Advanced\Seminar08')

# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию возьмите pickle версию файла из задачи 4 семинара. Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv


def pickle_to_csv(pk_file, csv_file):
    with open(pk_file, "rb") as source:
        data = pickle.load(source)
    with open(csv_file, 'w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    pickle_to_csv("test.pickle", "test.csv")