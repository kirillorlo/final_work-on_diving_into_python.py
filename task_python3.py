# tsk 1
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.9,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }

# max_weight = 1
# backpack = {}

# for i, weight in items.items():
#     if weight <= max_weight:
#         backpack[i] = weight
#         max_weight -= weight

# print(backpack)

# tsk 2
# text = 'Hello world. Hello Python. Hello again.'
# import re
# from collections import Counter

# cler_text = ''.join(char.lower() if char.isalpha() or
#     char.isspace() else ' ' for char in text)
# print(cler_text)

# words = cler_text.split() 
# print(words)
# words_count = {}
"""
    здесь пробуем комментить свой код
    функции незнакомы мне, но все работает)))
"""
# for word in words:
#     if word not in words_count:
#         words_count[word] = 1
#     else:
#         words_count[word] += 1

#print(words_count)

#top_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10]
#print(top_words)

# tsk 3

# lst = [5, 8, 9, 1, 1, 2, 2, 9, -5, 3, 3, -8]
# numbers = []
# for i in lst:
#     if i not in numbers:
#         numbers.append(i)
# numbers = sorted(numbers)
# print(numbers)
