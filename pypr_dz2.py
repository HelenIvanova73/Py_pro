'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.'''
BASE_SS = 16
LETTERS = 'abcdef'
def covert_to_another_ns(number):
    newnumber = ''
    while number > 0:
        number, remainder = divmod(number, BASE_SS)
        if remainder > 9:
            letter_index = remainder - 10
            remainder = LETTERS[letter_index]
        newnumber = str(remainder) + newnumber
    return newnumber


number = int(input('Введите целое число: '))
if covert_to_another_ns(number) == hex(number)[2:]:
    answer = f'Число {number = } в {BASE_SS}-ичной системе счисления = {covert_to_another_ns(number).upper()}'
else:
    answer = 'Перевод не удался'
print(answer)


'''Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.'''

import math, fractions

def join_string(a, b):
    return str(a) + '/' + str(b)

def split_string(s):
    return map(int, s.split('/'))

def reduce_fraction(a, b):
    gcd_ab = math.gcd(a, b)
    if gcd_ab > 1:
        a //= gcd_ab
        b //= gcd_ab
    return a, b

def add_fractions(a, b, a1, b1):
    result_numerator = a * b1 + b * a1
    result_denomerator = b * b1
    return join_string(*reduce_fraction(result_numerator, result_denomerator))

def product_fractions(a, b, a1, b1):
    result_numerator = a * a1
    result_denomerator = b * b1
    return join_string(*reduce_fraction(result_numerator, result_denomerator))


a, b = split_string( input('Enter first fraction like a/b: '))
a1, b1 = split_string( input('Enter second fraction like a/b: '))
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(a1, b1)
if str(f1 * f2) == product_fractions(a, b, a1, b1) and str(f1 + f2) == add_fractions(a, b, a1, b1):
    result = \
        f'{join_string(a, b)} + {join_string(a1, b1)} = {add_fractions(a, b, a1, b1)}\n{join_string(a, b)} * {join_string(a1, b1)} = {product_fractions(a, b, a1, b1)}'
else:
    result = 'error'
print(result)