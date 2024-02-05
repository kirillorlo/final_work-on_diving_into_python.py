from typing import Callable


# def add_str_one(a: str) -> Callable[[str], str]:
#     def add_str_two(b: str) -> str:
#         return a + ' - ' + b
#     return add_str_two

# word_one1 = add_str_one('Hi!')
# word_one2 = add_str_one('Привет!')

# print(word_one1('Kiryll'))
# print(word_one2('Katya'))

def add_one_str(a: str) -> Callable[[str], str]:
    names = ''

    def add_two_str(b: str) -> str:
        nonlocal names
        names = names + ', ' + b
        return a + names
    return add_two_str


hi = add_one_str('Hello')


print(hi('Katya'))
print(hi('Kiryll'))

def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc


small = main(42)
big = main(73)
print(small(7))
print(big(7))
print(small(10))
