'''1. Напишите функцию для транспонирования матрицы'''


NUMBER_OF_ROWS = 5
NUMBER_OF_COLUMNS = 5
MIN_NUMBER = -10
MAX_NUMBER = 10

from random import randint


def create_matrix() -> list[list[int]]:
    return [[randint(MIN_NUMBER, MAX_NUMBER + 1) for _ in range(NUMBER_OF_COLUMNS)] for _ in range(NUMBER_OF_ROWS)]


def print_matrix(my_list: list[list[int]]):
    nor = len(my_list)

    noc = len(my_list[0])
    for i in range(nor):
        for j in range(noc):
            print(f'{my_list[i][j]: > 4}', end=' ')
        print()


def matrix_transposition(my_list):# list[list[int]]) -> list[list[int]]:
    a = [[0 * 5]] * 5
    for i in range(4):#NUMBER_OF_ROWS):
        for j in range(4):#NUMBER_OF_COLUMNS):
            a[j][i] = 5#my_list[i][j]
    return type(a)

print_matrix(create_matrix())
print()
print(matrix_transposition(create_matrix()))




'''2.Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.'''

'''3. Напишите программу банкомат. 
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.'''