# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

# import sys

# from typing import Hashable

# data = [1, 2., '3', [4], (5,)]

# for n, obj in enumerate(data, 1):
#     print(f'{n} {obj} {id(obj)} {sys.getsizeof(obj)} '
#           f'{hash(obj) if isinstance(obj, Hashable) else "Объект нехэшируемый"}'
#           f'{" Число целое" if isinstance(obj, int) else ""} '
#           f'{"Строка" if isinstance(obj, str) else ""}')

# number = 10
# number_two = number
# res = ''
# while number != 0:
#     res = str(number % 2) + res
#     number //= 2
# print(res)
# print(bin(number_two))
# number = 10
# number_two = number
# res = ''
# while number != 0:
#     res = str(number % 8) + res
#     number //= 8
# print(res)
# print(oct(number_two))Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не превышает 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

# import math

# import decimal

# diameter = float(input())
# decimal.getcontext().prec = 48

# radius = decimal.Decimal(diameter/2)
# PI = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
# area = PI * radius**2
# length = 2*PI * radius
# print(f"Площадь круга: {area}")
# print(f"Длина окружности: {length}")

# корни дискриминанта
# a, b, c = 1, -2, 20
# d = b ** 2 - 4 * a * c

# if d < 0:
#     print('Нет действительных корней.')
#     print('Дискриминант ', d)
#     x1 = (-1 * b + d ** .5) / 2 * a
#     x2 = (-1 * b - d ** .5) / 2 * a
#     print('Сопряженные комплексные корни', x1, 'и', x2)
# elif d == 0:
#     x = -1 * b / 2 * a
#     print('Один действительный корень.')
# else:
#     x1 = (-1 * b + d ** .5) / 2 * a
#     x2 = (-1 * b - d ** .5) / 2 * a
#     print('Два действительных корня', x1, 'и', x2)

# strings = ["1", "2", "3", "4", "5"]
# numbers = list(map(int, strings))
# print(numbers)  # Выводит: [1, 2, 3, 4, 5]




