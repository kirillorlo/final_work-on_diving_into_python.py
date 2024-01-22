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