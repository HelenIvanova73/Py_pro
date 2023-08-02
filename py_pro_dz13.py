# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.

# нельзя создавать прямоугольник со сторонами
# отрицательной длины.
from math import pi

class CalcError(Exception):
    pass


class NegativeValueError(CalcError):
    def __int__(self, value):
        self.value =value
    def __str__(self):
        return f'Вы ввели отрицательное значение. Радиус окружности должен быть > 0.'


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise NegativeValueError
        else:
            self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

circle1 = Circle(-5)
circle2 = Circle(6)
print(f'{circle1.get_area() = }')
print(circle2.get_area())