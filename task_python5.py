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
# print(dict_1)

