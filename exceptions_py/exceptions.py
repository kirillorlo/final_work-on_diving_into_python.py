# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as k:
#             print(f'Ваш код привел к ошибке: {k}')
#     return num

# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')

# MAX_COUNT = 5
# result = None

# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         result = 100 / num
#         break

# print(f'{result = }')

MAX_COUNT = 5
res = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('введите целое число: '))
        print('Успешно получили целое число! Ура!')
    except ValueError as error:
        print(f'Попытка {count} завершилась ошибкой {error}')
    else:
        try:
            res = 100 / num
        except ZeroDivisionError as error:
            print('Результат деления на ноль!')
            res = float('inf')
        break

print(f'{res = }')