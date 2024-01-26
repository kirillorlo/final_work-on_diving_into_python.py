# data = {'one': 1, 'two': 2}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)
# a = 8
# b = 10
# print(f'{a=}\t{b=}')
#data = {2, 3, 4, 10, 11, 8, 9}
# res = []
# for i in data:
#     if i % 2 == 0:
#         res.append(i) 
# print(res)
#res =[i for i in data if i % 3  == 0]
#data = {2, 3, 4, 10, 11, 8, 9}
#res1 = ( i for i in data if i > 4)
#print(res1)
# Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь, где:
# второе и третье число являются ключами
# первое число является значением для первого ключа
# четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа

# numbers = input("Введите 4 числа, разделенных /: ")
# first, second, third, *forth = map(int, numbers.split('/'))
# numb_dict = {second:first, third: tuple(forth)}
# print(numb_dict)

#Самостоятельно сохраните в переменной строку текста. Создайте из строки словарь, #где ключ - буква, а значение - код буквы. Напишите преобразование в одну строку.
# text = 'hsafapwr'
# dict_1 = {item: ord(item) for item in text}
# d = iter(dict_1.items())
# for _ in range(5):
#     print(next(d))

# Создайте генератор чётных чисел от нуля до 100. Из последовательности исключите числа, сумма цифр которых равна 8. Решение в одну строку.

# list_1 = [i for i in range(2, 100, 2) if i % 10 + i // 10 != 8]
# print(list_1)
# list_0 = [i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8]
# print(list_0)

#Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔️ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔️ Вместо чисел, кратных пяти — слово «Buzz».
# ✔️ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔️ *Превратите решение в генераторное выражение.

# for i in range(101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# print(*['FizzBuzz' if i % 15 == 0
#     else 'Fizz' if i % 3 == 0
#     else 'Buzz' if i % 5 == 0
#     else i for i in range(101)], sep='\n')

# Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2. Для проверки числа на простоту используйте правило: “число является простым, если делится нацело только на единицу и на себя”.
# Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
#Для проверки числа на простоту используйте правило: “число является простым,
# если делится нацело только на единицу и на себя”.

# def is_simple(n:int) -> bool:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def simple_generate(number: int):
#     i = 2
#     yield i
#     i += 1
#     while i <= number:
#         if is_simple(i):
#             yield i
#         i += 2

# a = simple_generate(27)
# for _ in range(27):
#     print(next(a), end=' ')


# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# file_path = "C:/Users/User/Documents/example.txt")

# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     print(file_name)
#     file_extension = file_name.split(".")[-1]
#     print(file_extension)
#     path = file_path[:-len(file_name)]
#     print(path)
#     print(-len(file_name))
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)

# print(get_file_info(file_path = "C:/Users/User/Documents/example.txt"))
# a = 'qwerty'
# b = a.split('e')[-1]
# print(b)
# print(a[:-len(b)])

# задача по Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

for i in range(10):
    print(next(f))
