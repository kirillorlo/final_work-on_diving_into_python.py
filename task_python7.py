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

from string import ascii_lowercase

from random import choice, randint

VOWELS = 'a', 'o', 'e', 'i', 'u', 'y'
LETTERS = ascii_lowercase


def generate_pseudonyms(min_len=3, max_len=6) -> str:
    name = choice(VOWELS).upper() + ''.join(choice(LETTERS) for _ in range(randint(min_len, max_len)))
    return name


def save_name_to_file(file_name: str, rows: int):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(generate_pseudonyms() for _ in range(rows)))


if __name__ == '__main__':
    save_name_to_file('names.txt', 5)

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
