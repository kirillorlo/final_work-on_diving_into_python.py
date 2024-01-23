# tsk 1
# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает транспонированную матрицу.

# def transpose(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
    
#     return transposed

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# print(transpose(matrix))

# tsk 2
# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if isinstance(value, (int, str, float, bool, tuple)):
#             result[value] = key
#         else:
#             result[str(value)] = key
        
#     return result

# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)

# tsk 3
# задача про банк
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

# Введите ваше решение ниже

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False
    return True

def deposit(amount):
    """Пополнение счета"""
    global bank_account, count
    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False  # Операция не выполнена из-за некратной суммы
    count += 1
    bank_account += amount
    operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    return True


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    percent = amount * PERCENT_REMOVAL
    percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е.')

def exit():
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

deposit(1000)
withdraw(200)
exit()

print(*operations)





