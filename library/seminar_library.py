# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл. Например отлавливаем ошибку деления на ноль.

# import logging

# logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.NOTSET)


# def division(x: int | float, y: int | float):
#     try:
#         res = x / y
#         logging.debug(f"x / y = {res}")
#         return res
#     except ZeroDivisionError as err:
#         logging.error(f'{err}: На ноль делить нельзя')


# if __name__ == '__main__':
#     division(3, 0)
#     division(3, 5)
#     division(3, 1)

# На семинаре про декораторы был создан логирующих декоратор. Он сохранял аргументы функции и результат её работы в файл. Напишите аналогичный декоратор, но внутри используйте модуль logging.

# import logging


# def log_decorator(func):

#     def wrapper(*args, **kwargs):

#         logging.basicConfig(filename=f'{func.__name__}.log', encoding='utf-8', level=logging.NOTSET)
#         res = func(*args, **kwargs)
#         logging.debug(f'{args} {kwargs} {res}')
#         return res

#     return wrapper


# @log_decorator
# def division(x: int | float, y: int | float):
#     try:
#         return x / y       
#     except ZeroDivisionError as err:
#         return float('inf')


# if __name__ == '__main__':
#     division(2, 0)

# Доработаем задачу 2. Сохраняйте в лог файл раздельно: уровень логирования, дату события, имя функции (не декоратора), аргументы вызова, результат.

# import logging
# from functools import wraps

# FORMAT = '{levelname:<8} - {asctime}. В функции {funcName} {msg}'
# logging.basicConfig(format=FORMAT, filename='Task_3.log', encoding='utf-8', style='{', level=logging.NOTSET)

# def log_decorator(func):
#     logger = logging.getLogger(__name__)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         # logger.debug(f'{func.__name__} {args} {kwargs} {res}')
#         logger.debug(f'{args} {kwargs} {res}')
#         return res
#     return wrapper


# @log_decorator
# def division(x: int | float, y: int | float):
#     try:
#         return x / y
#     except ZeroDivisionError as err:
#         return float('inf')


# if __name__ == '__main__':
#     division(2, 5)

# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п. Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime, date
from task03 import log_decorator

MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


@log_decorator
def string_to_date(s: str) -> datetime:
    weeks, weekday, month = s.split()

    weeks = int(weeks[0])
    y = datetime.now().year
    month_num = MONTHS.index(month) + 1
    weekday = DAYS.index(weekday) + 1
    first_day = date(day=1, month=month_num, year=y).isoweekday()  # 1-7

    day_by_date = ((1 + 7 * weeks - (first_day - weekday))
                   if weekday < first_day else 1 + 7 * (weeks - 1) - (first_day - weekday))
          
    return datetime(day=day_by_date, month=month_num, year=y)


if __name__ == '__main__':
    string_to_date('1-й четверг ноября')
    string_to_date('1-е воскресенье февраля')
    string_to_date('5-й четверг февраля')
    string_to_date('5-е воскресенье марта')
    string_to_date('5-е воскресенье марта')
    string_to_date('5-е пятница мая')

# Дорабатываем задачу 4. Добавьте возможность запуска из командной строки. При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

