#Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. Первое число int, второе - float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000. Количество строк и имя файла передаются как аргументы функции.
# from random import randint, uniform
# MIN_NUM = -1000
# MAX_NUM = 1000


# def write_numbers(name, rows):
#     with open(name, 'w') as f:
#         for i in range(rows):
#             f.write(f'{randint(MIN_NUM, MAX_NUM)} | '
#                     f'{uniform(MIN_NUM, MAX_NUM)}\n')

# if __name__ == '__main__':
#     write_numbers('numbers1.txt', 20)

# Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.

# from string import ascii_lowercase

# from random import choice, randint

# VOWELS = 'a', 'o', 'e', 'i', 'u', 'y'
# LETTERS = ascii_lowercase


# def generate_pseudonyms(min_len=3, max_len=6) -> str:
#     name = choice(VOWELS).upper() + ''.join(choice(LETTERS) for _ in range(randint(min_len, max_len)))
#     return name


# def save_name_to_file(file_name: str, rows: int):
#     with open(file_name, 'w', encoding='utf-8') as f:
#         f.writelines('\n'.join(generate_pseudonyms() for _ in range(rows)))


# if __name__ == '__main__':
#     save_name_to_file('names.txt', 5)

#Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более короткого файла, возвращайтесь в его начало
# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#   ✔ если результат умножения отрицательный, сохраните имя
#       записанное строчными буквами и произведение по модулю
#   ✔ если результат умножения положительный, сохраните имя
#       прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
# from string import ascii_lowercase
# VOWELS = 'a', 'o', 'e', 'i', 'u', 'y'
# LETTERS = ascii_lowercase

# def get_file_number_of_lines(file) -> int:
#     with open(file, 'r') as f:
#         return len(f.readlines())
#         # return sum(1 for i in f if i)


# def read_or_begin(file) -> str:
#     current = file.readline().rstrip()
#     if not current:
#         file.seek(0)
#         current = file.readline().rstrip()
#     return current


# def combine_two_files(file1, file2, output):
#     len_f1 = get_file_number_of_lines(file1)
#     len_f2 = get_file_number_of_lines(file2)

#     with (
#         open(file1, 'r') as f1,
#         open(file2, 'r') as f2,
#         open(output, 'w') as out,
#     ):
#         # print(type(f1), type(f2), type(out))  # <class '_io.TextIOWrapper'>
#         for _ in range(max(len_f1, len_f2)):
#             name = read_or_begin(f1)
#             numbers = read_or_begin(f2)

#             a, b = numbers.replace(' ', '').split('|')
#             mul = float(a) * float(b)

#             if mul < 0:
#                 out.write(f'{name.lower()} {abs(mul)}\n')
#             else:
#                 out.write(f'{name.upper()} {round(mul)}\n')


# if __name__ == '__main__':
#     # print(get_file_number_of_lines('numbers.txt'))
#     # print(get_file_number_of_lines('names.txt'))
#     combine_two_files('names.txt', 'numbers.txt', 'output.txt')

#Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
# import os
# from string import ascii_lowercase
# from random import choice, randint
# VOWELS = 'a', 'o', 'e', 'i', 'u', 'y'
# LETTERS = ascii_lowercase

# def create_files_ext (ext, min_name_len=6, max_name_len=30, min_bytes=256, max_bytes=4096, num_files=42):
#     for _ in range(num_files):
#         file_name = generate_pseudonyms(min_name_len, max_name_len) + ext
#         file_size = randint(min_bytes, max_bytes)
#         byte_list = bytes(randint(0,255) for _ in range(file_size))
#         with open (file_name, 'wb') as f:
#             f.write(byte_list)
#         print(f"Создан файл {file_name} размером {os.path.getsize(file_name)} байт")
# def generate_pseudonyms(min_len=3, max_len=6) -> str:
#     name = choice(VOWELS).upper() + ''.join(choice(LETTERS) for _ in range(randint(min_len, max_len)))
#     return name

# if __name__ == '__main__':
#     create_files_ext(".pdf", num_files=3)


# # Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории

# import os


# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []
#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')
#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]
#     # Сортируем файлы по имени
#     filtered_files.sort()
#     # Задаем начальный номер для порядкового номера
#     num = 1

#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]
#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]
        
#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num)/zfill(num_digits) + '.' + target_ext

#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)

#         # Увеличиваем порядковый номер
#         num += 1
# Введите ваше решение ниже
code_to_write = '''
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    new_names = []

    files = os.listdir('geekbrains')

    filtered_files = [file for file in files if file.endswith(source_ext)]

    filtered_files.sort()

    num = 1

    for file in filtered_files:
        name = os.path.splitext(file)[0]

        if name_range:
            name = name[name_range[0]-1:name_range[1]]

        new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

        os.rename(file, new_name)

        new_names.append(new_name)

        num += 1

    return new_names
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)
