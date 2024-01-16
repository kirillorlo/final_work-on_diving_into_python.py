# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# res = len(set(list1).intersection(set(list2)))
# print(f'Количество совпадающих чисел: {res}')

# a = 2
# b = 444
# c = 4

# def triangle_check(a, b, c):
#     if a + b > c and b + c > a and c + a > b:
#         print('Треугольник существует')
        
#         if a == b == c:
#             print('Треугольник равносторонний')
#         if a != b and  a != c and c != b:
#             print('Треугольник разносторонний')
#         if a == b != c or a != c == b:
#             print('Треугольник рвнобедренный')


    
#     else:
#         print('Треугольник не существует')

# triangle_check(a, b, c)

# num = 3
# divider_counter = 1               # Определяем счетчик делителя
# number_of_divisions = 0           # Определяем количество делений с нулевым остатком

# if num >= 2 and num < 100000:
#     while divider_counter <= num:
#         res = num % divider_counter 
#         if res == 0:
#             divider_counter += 1
#             number_of_divisions += 1   
#         else:
#             divider_counter += 1

# if number_of_divisions == 2:
#     print('Простое')
# elif number_of_divisions > 2:
#     print('Не является простым')
# else:
#     print('Число должно быть больше 1 и меньше 100000')   

# num = -10
# if not 1 < num <= 100000:
#     print('Не то число! Смотри диапазон в коде!')
# else:
#     #is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         print(int(num ** 0.5) + 1)
#         if num % i == 0:
#             print(num, i)
#             print('Не простое')
#             break
#     else:
#         print('Простое')


# палиндром
# str = 'abba1'
# if str == ''.join(reversed(str)):
#     print('Это палиндром!')
# else:
#     print('Не является палиндромом')
# str1 = str[::-1]
# print(str1)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []

# print([i for i in a if i < 5])
#Посчитайте сумму чётных элементов от 1 до n исключая кратные e. #Используйте while и if. Попробуйте разные значения e и n.


# Напишите программу, которая запрашивает год и проверяет его на високосность. 
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

# MAIN_CONDITION = 4
# ADD_CONDITION = 100
# YEAR_EXCEM = 400

# year = int(input('Введите год '))

# if (year % MAIN_CONDITION == 0 and year % ADD_CONDITION != 0
#         or year % YEAR_EXCEM == 0):
#     res = 'Год +'
# else:
#     res = 'Год -'

# print(res)

# while True:
#     number = int(input('Введите чило: '))
#     if not 1 < number < 1000:
#         continue
#     if number < 10:
#         res = number**2
#     elif number < 100:
#         res = (number // 10) * (number % 10)
#     else:
#         res = (number % 10 * 100) + (number // 10 % 10 * 10) + number // 100
#     break

# print(res)

# for i in range(2, 10, 4):
#     for j in range(2, 11):
#         for k in range(i, i+4):
#             print(f"{k:>1} X {j:>2} = {k*j:>2}", end="\t")
#         print()
#     print()

# stars_row = int(input('Enter number: '))

# for i in range(stars_row):
#     print((stars_row - i) * ' ' + ((2 * i) + 1) * '*')
# for i in range(5):
#     print(i)

# data = input('Enter info: ')
# a = data
# print(type(data))
# print(id(data))
# print(hash(a))
# a = 'sss'
# print(hash(a))
# num = 255
# a = hex(num)
# b = a[2:]
# res = b.upper()
# if num == 0:
#     print('Шестнадцатеричное представление числа: ')
#     print('Проверка результата: 0x0')
# else:
#     print(f'Шестнадцатеричное представление числа: {res}')
#     print(f'Проверка результата: {a}')

