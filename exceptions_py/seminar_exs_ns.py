#Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число. Обрабатывайте не числовые данные как исключения.
# def enter_number():
#     while True:
#         try:
#             number = int(input('Enter number: '))
#             return print(f'{number}')
#         except ValueError:
#             print('Wrong data')

# enter_number()

# Создайте функцию аналог get для словаря. Помимо самого словаря функция принимает ключ и значение по умолчанию. При обращении к несуществующему ключу функция должна возвращать дефолтное значение. Реализуйте работу через обработку исключений.

# def get_dict(dictionary, key, default_value=None):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return default_value

# my_dict = {'one': 1, 'two': 2, 'three': 3}
# key_control = 'qwerty'

# print(get_dict(my_dict, key_control))
# print(get_dict(my_dict, key='two'))
# print(get_dict(my_dict, key='wrong', default_value=15))

# Создайте класс с базовым исключением и дочерние классы-исключения: ошибка уровня, ошибка доступа.

class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    pass


class AccessError(ProjectException):
    pass
