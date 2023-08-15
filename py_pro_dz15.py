'''Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.'''
'''import argparse
import math
import logging

parser = argparse.ArgumentParser(description='калькулятор')
parser.add_argument('operation', help='выберите операцию: +, -, *, /, sin, cos, tan, log, sqrt, quit')
parser.add_argument('num1', type=float, help='первое число')
parser.add_argument('num2', type=float, nargs='?', default=None, help='второе число (только для арифметических операций)')

args = parser.parse_args()

FORMAT = '{levelname:<8} - {asctime} Записано сообщение: {message}'

logging.basicConfig(filename='work_2.log.', format=FORMAT, style='{', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


if args.operation in ['sin', 'cos', 'tan', 'log', 'sqrt']:

    if args.operation == 'sin':
        result = math.sin(args.num1)
    elif args.operation == 'cos':
        result = math.cos(args.num1)
    elif args.operation == 'tan':
        result = math.tan(args.num1)
    elif args.operation == 'log':
        try:
            result = math.log(args.num1)
        except ValueError:
            logger.error('Нельзя получить логарифм отрицательного числа')
            result = None

    elif args.operation == 'sqrt':
        try:
            result = math.sqrt(args.num1)
        except ValueError:
            logger.error('Нельзя получить корень отрицательного числа')
            result = None
    print('Результат:', result)


else:

    if args.operation == '+':
        result = args.num1 + args.num2
    elif args.operation == '-':
        result = args.num1 - args.num2
    elif args.operation == '*':
        result = args.num1 * args.num2
    elif args.operation == '/':
        try:
            result = args.num1 / args.num2
        except ZeroDivisionError:
            logger.error('Деление на ноль')
            result = None
    print('Результат:', result)



# запуск из командной строки:
# python .\home_work_2.py sqrt 16
# python .\home_work_2.py log -16
# python .\home_work_2.py / 2 0'''
# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# текст задачи
'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c — 
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
import argparse
import logging


FORMAT = '{levelname:<8} - {asctime}. Записано сообщение: {msg}'
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)
formatter = logging.Formatter(FORMAT, style='{')
error_handler = logging.FileHandler('errors_.log', encoding='utf-8')
error_handler.setFormatter(formatter)
error_logger.addHandler(error_handler)


def triangle(a, b, c):

    maximum = max(a, b, c)
    if maximum < a + b + c - maximum:
        try:
            if a == b == c:
                result = 'треугольник равносторонний'
            elif a == b or b == c or a == c:
                result = 'треугольник равнобедренный'
            else:
                result = 'треугольник разносторонний'
            return result
        except Exception as err:
            error_logger.error('треугольник не существует')


parser = argparse.ArgumentParser(description='определям вид треугольника')
parser.add_argument('a', type=float, help='сторона a')
parser.add_argument('b', type=float, help='сторона b')
parser.add_argument('c', type=float, help='сторона c')

args = parser.parse_args()
result_ = triangle(args.a, args.b, args.c)
print(result_)


# для проверки в командной строке: python py_pro_dz15.py 1 2 3