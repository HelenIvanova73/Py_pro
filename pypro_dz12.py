'''Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
'''
import csv
from random import randint

class Student:
    def __init__(self, fullname, subjects={}):
        if all(x.isalpha() and x.istitle() for x in fullname.split()):
            self.fullname = fullname
        else:
            raise ValueError(f'ФИО должно состоять из букв и все слова начинаются с заглавной')
        #self.fullname = fullname
        self.subjects = subjects

    '''
        ALSO, WARUM DIESER TEIL NICHT FUNCTIONIERT, WEI$ ICH NICHT
        
        
    @property
    def fullname(self):
        return self.fullname

    @fullname.setter
    def fullname(self, value):
        if all(x.isalpha() and x.istitle() for x in value.split()):
            self.fullname = value
        else:
            raise ValueError(f'ФИО должно состоять из букв и все слова начинаются с заглавной')'''

    @property
    def get_subjects_dict(self):           # получаем предметы из csv и записываем оценки
        #self.subjects = {}
        with open('subjects_.csv', 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.subjects[row[0]] = {'scores': [randint(2, 5) for i in range(5)],
                                    'tests': [randint(0, 100) for i in range(5)]}
        return (self.subjects)
    def set_subjects(self, subjects):
        self._subjects = subjects

    @property
    def get_average_test_score(self):  # вычисляем средние оценки
        subject = self.subjects
        aver_scores = [sum(list(i.values())[0]) / 5 for i in self.subjects.values()]
        aver_tests = [sum(list(i.values())[1])/5 for i in self.subjects.values()]
        return aver_scores, aver_tests
    def __str__(self):
        return f'Student(name={self.fullname}\n subjects and scores:{self.get_subjects_dict}\n average scores and tests results: {self.get_average_test_score} )'

std1 = Student('Gvido Van Rossum')
print(std1)
std2 = Student('Albert whoisit Einstein')
print(std2)

std3 = Student('Albert whoisit 1stein')
print(std3)