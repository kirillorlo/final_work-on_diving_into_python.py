# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
# import random


# def guess(min_numb, max_numb, count):
#     numb_1 = random.randint(min_numb, max_numb)
#     for i in range(count):
#         nubm = int(input('Enter number: '))
#         if nubm == numb_1:
#             return True
#         elif nubm > numb_1:
#             print('Число меньше загаданного')
#         else:
#             print('Число больше загаданного')
#     return False


# if __name__  == '__main__':
#     print(guess(2, 10, 3))

# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
# import random
# from sys import argv

# def guess(min_numb, max_numb = 10, count = 3):
#     numb_1 = random.randint(min_numb, max_numb)
#     for i in range(count):
#         nubm = int(input('Enter number: '))
#         if nubm == numb_1:
#             return True
#         elif nubm > numb_1:
#             print('Число меньше загаданного')
#         else:
#             print('Число больше загаданного')
#     return False


# if __name__  == '__main__':
#     print(guess(*list(map(int, argv[1:]))))

# Создайте модуль с функцией внутри. Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание. Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.'Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна']
# def secrets(riddle: str, answers: list[str], counter: int) -> int:
#     print(riddle)
#     for i in range(counter):
#         ans = input("Введите ответ: ")
#         if ans in answers:
#             return i + 1
#     return 0


# if __name__ == '__main__':
#     print(secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'], 3))

# Добавьте в модуль с загадками функцию, которая хранит словарь списков. Ключ словаря - загадка, значение - список с отгадками. Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],'Не лает, не кусает, в дом не пускает': ['замок'],'Сидит дед во сто шуб одет': ['лук', 'луковица'],
# def secrets(riddle: str, answers: list[str], counter: int) -> int:
#     print(riddle)
#     for i in range(counter):
#         ans = input("Введите ответ: ")
#         if ans in answers:
#             return i + 1
#     return 0


# def test_storage():
#     dict_riddle = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
#         'Не лает, не кусает, в дом не пускает': ['замок'],
#         'Сидит дед во сто шуб одет': ['лук', 'луковица']}
#     for test_data in dict_riddle.items():
#         print(secrets(*test_data, counter=3))


# if __name__ == '__main__':
#     # print(secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'], 3))
#     test_storage()

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). Функция формирует словарь с информацией о результатах отгадывания. Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. Для формирования результатов используйте генераторное выражение.

# _results = dict()


# def secrets(riddle: str, answers: list[str], counter: int) -> int:
#     print(riddle)
#     for i in range(counter):
#         ans = input("Введите ответ: ")
#         if ans in answers:
#             answer_counter(riddle, i + 1)
#             return i + 1
#     answer_counter(riddle, 0)
#     return 0


# def test_storage():
#     dict_riddle = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
#                    'Не лает, не кусает, в дом не пускает': ['замок'],
#                    'Сидит дед во сто шуб одет': ['лук', 'луковица']}
#     for test_data in dict_riddle.items():
#         print(secrets(*test_data, counter=3))


# def answer_counter(riddle: str, result: int):
#     global _results
#     _results.setdefault(riddle, result)


# def print_results():
#     global _results
#     for k, v in _results.items():
#         print(f'{k=}, {v=}')


# if __name__ == '__main__':
#     # print(secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'], 3))
#     test_storage()
#     print_results()


# MONTHS = {
#     1: range(1, 32),
#     2: range(1, 29),
#     3: range(1, 32),
#     4: range(1, 31),
#     5: range(1, 32),
#     6: range(1, 31),
#     7: range(1, 32),
#     8: range(1, 32),
#     9: range(1, 31),
#     10: range(1, 32),
#     11: range(1, 31),
#     12: range(1, 32),
# }


# # from datetime import datetime
# # d = datetime()

# def parse_data(date: str) -> bool:
#     d, m, y = map(int, date.split('.'))
#     return _y_is_valid(y) and _m_is_valid(m) and _d_is_valid(d, m, y)


# def _d_is_valid(d: int, m: int, y: int) -> bool:
#     if _is_leap_year(y) and m == 2:
#         return d in range(1, 30)
#     return d in MONTHS[m]


# def _m_is_valid(m: int) -> bool:
#     return m in range(1, 13)


# def _y_is_valid(y: int) -> bool:
#     return y in range(1, 10_000)


# def _is_leap_year(y: int) -> bool:
#     return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

# 22:09
# from data_parser import parse_data as pd

# print(pd('28.02.2000'))
# print(pd('29.02.2024'))
# print(pd('28.02.1900'))
# print(pd('28.02.0001'))
# print(pd('30.02.2010'))

# import random
# from itertools import combinations

# def generate_board():
#     # Генерируем случайную доску
#     board = []

#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board

# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True

# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     board_list = []
#     while len(board_list) < 4:
#         board = generate_board()
#         if check_queens(board):
#             board_list.append(board)
#     return board_list

# board_list = generate_boards()
# if len(board_list) != 4:
#     print("Вы собрали не то количество комбинаций")
# else:
#     print("Отлично!")

# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нетВаша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

from sys import argv

date_for_verification = '15.07.2000'


def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


def valid(full_date: str):
    date, month, year =(int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False  
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True


if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_for_verification))



