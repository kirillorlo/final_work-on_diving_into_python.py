# # Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest
from task_test import clear_text

class TestClearText(unittest.TestCase):
    def test_no_changes(self):
        self.assertEqual(clear_text('hello world'), second='hell world', msg=' Всё поломали!!!')
    
    def test_registr(self):
        self.assertEqual(clear_text('hELLo World'), second='hello world')
    
    def test_delete_punctuation(self):
        self.assertEqual(clear_text('hello,, world!'), second='hello world')

    def test_delete_alpha(self):
        self.assertEqual(clear_text('hello мир'), second='hello ')

    def test_all(self):
        self.assertEqual(clear_text('hELLo,мир World!'), second='hello world')

if __name__ == '__main__':
    unittest.main(verbosity=4)