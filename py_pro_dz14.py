'''Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах: doctest, unittest, pytest.'''
# текст задачи
'''Задача1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c — 
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой 
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
равнобедренным или равносторонним.
Напишем для задачи 1 тесты doctest. Проверим следующие варианты:
●	треугольник не существует
●	треугольник разносторонний
●	треугольник равнобедренный
●	треугольник равносторонний
'''

# вариант doctest
'''

import doctest


def triangle_test(a, b, c) -> str:
    """
    >>> triangle_test(2, 4, 6)   #  треугольник не существует
    'треугольник не существует'
    >>> triangle_test(2, 6, 5)   #  треугольник разносторонний
    'треугольник разносторонний'
    >>> triangle_test(5, 5, 3)    #  треугольник равнобедренный
    'треугольник равнобедренный'
    >>> triangle_test(1, 1, 1)   #  треугольник равносторонний
    'треугольник равносторонний'
    """

    maximum = max(a, b, c)
    if maximum >= a + b + c - maximum:
        result = 'треугольник не существует'
    elif a == b == c:
        result = 'треугольник равносторонний'
    elif a == b or b == c or a == c:
        result = 'треугольник равнобедренный'
    else:
        result = 'треугольник разносторонний'
    return result
    
    doctest.testmod(verbose=Тrue)'''

#  вариант unittest
'''

import unittest

class TestTriangle(unittest.TestCase):

    def test_not_ecxist(self):
        self.assertEqual(triangle(2, 4, 6), 'треугольник не существует')

    def test_scalene_triangle(self):
        self.assertEqual(triangle(2, 6, 5), 'треугольник разносторонний')

    def test_isosceles_triangle(self):
        self.assertEqual(triangle(5, 5, 3), 'треугольник равнобедренный')

    def test_equillateral_triangle(self):
        self.assertEqual(triangle(42, 42, 42), 'треугольник равносторонний')


def triangle(a, b, c):
    maximum = max(a, b, c)
    if maximum >= a + b + c - maximum:
        result = 'треугольник не существует'
    elif a == b == c:
        result = 'треугольник равносторонний'
    elif a == b or b == c or a == c:
        result = 'треугольник равнобедренный'
    else:
        result = 'треугольник разносторонний'

    return result

if __name__ == '__main__':
    unittest.main(verbosity=2)'''

#  вариант pytest
import pytest
  

def test_not_exist(*args, **kwargs):
    assert triangle(2, 4, 6) == 'треугольник не существует'


def test_scalene_triangle(*args, **kwargs):
    assert triangle(2, 6, 5) == 'треугольник разносторонний'
    
def test_isosceles_triangle(*args, **kwargs):
    assert triangle(5, 5, 3) == 'треугольник равнобедренный'

def test_equillateral_triangle(*args, **kwargs):
    assert triangle(42, 42, 42) == 'треугольник равносторонний'

def triangle(a, b, c):
    maximum = max(a, b, c)
    if maximum >= a + b + c - maximum:
        result = 'треугольник не существует'
    elif a == b == c:
        result = 'треугольник равносторонний'
    elif a == b or b == c or a == c:
        result = 'треугольник равнобедренный'
    else:
        result = 'треугольник разносторонний'
    return result


if __name__ == '__main__':
    pytest.main(['-v'])

