from typing import Callable


def add_str_one(a: str) -> Callable[[str], str]:
    def add_str_two(b: str) -> str:
        return a + ' - ' + b
    return add_str_two

word_one1 = add_str_one('Hi!')
word_one2 = add_str_one('Привет!')

print(word_one1('Kiryll'))
print(word_one2('Katya'))
