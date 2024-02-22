# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов. Возвращается строка в нижнем регистре.

# from string import ascii_letters


# def clear_text(s: str) -> str:
#     chars = ascii_letters + ' '
#     return ''.join([c.lower() for c in s if c in chars])


# if __name__ == '__main__':
#     print(clear_text('Hello world'))


# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters


def clear_text(s: str) -> str:
    """
    >>> clear_text('hello world')
    'hello world'
    >>> clear_text('Hello world')
    'hello world'
    >>> clear_text('Hello world!')
    'hello world'
    >>> clear_text('Hello мир')
    'hello '
    >>> clear_text('Hello, world или мир!')
    'hello world  '
    """
    chars = ascii_letters + ' '
    return ''.join([c for c in s if c in chars]).lower()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)