'''2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
 В результирующем списке не должно быть дубликатов.'''
import string

N = 10
MIN_LIST = 0
MAX_LIST = 10

from random import randint


print('dz3 task2')
my_list = [randint(MIN_LIST, MAX_LIST) for i in range(N)]
print(f'{my_list = }')
new_list = list(set([i for i in my_list if my_list.count(i) > 1]))
print(f'{new_list = }')
print()

'''3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.'''


from string import punctuation
from collections import Counter


text = '''В 2000 году ядро команды разработчиков Python перешло в BeOpen.com, сформировав команду BeOpen PythonLab. CNRI потребовала 
выпустить версию 1.6, включающую всю разработку языка до момента ухода команды из корпорации. В результате графики выпуска версий 
1.6 и 2.0 имели значительное перекрытие[5]. Python 2.0 был единственным релизом BeOpen.com. После него Ван Россум и 
остальные разработчики PythonLab присоединились к Digital Creations.
Релиз 1.6 включал новое лицензионное соглашение от CNRI, которое было значительно длиннее лицензии CWI, использовавшейся ранее. 
Новая лицензия включала статью, что лицензионное соглашение регулируется законами штата Вирджиния. Фонд свободного программного обеспечения
 (FSF) заявил, что статья о выборе правовой нормы противоречит GNU GPL. BeOpen, CNRI и FSF договорились изменить свободную лицензию 
 Python, чтобы сделать её совместимой с GPL. Python 1.6.1 был по сути Python 1.6 с исправлением мелких ошибок и с новой
  GPL-совместимой лицензией[16].

Версия 2.0
В версии Python 2.0 появилось списковое включение — функция, заимствованная из функциональных языков программирования SETL и Haskell. Синтаксис в Python для этой конструкции очень похож на Haskell, за исключением того, что в Haskell предпочли использовать символы пунктуации, а в Python — ключевые слова. Также в Python 2.0 была добавлена система сборки мусора с поддержкой циклических ссылок[5].

Python 2.1 очень похож на Python 1.6.1 и Python 2.0. Лицензия, начиная с этой версии, была переименована в Python Software Foundation License. Начиная с альфа релиза Python 2.1 весь код, техническая документация и спецификации принадлежат некоммерческой организации Python Software Foundation (PSF), созданной в 2001 году по образцу Apache Software Foundation[16]. Релиз включал изменение в спецификацию языка, поддерживающее вложенные области видимости, как в языках со статической (лексической) областью видимости[17]. Эта возможность была выключена по умолчанию и не потребовалась до Python 2.2.
Главным нововведением в Python 2.2 было объединение базовых типов Python и классов, создаваемых пользователем, в одной иерархии. Это сделало Python полностью объектно-ориентированным языком[18]. Тогда же были добавлены генераторы, идея которых заимствована из Icon[19].
В ноябре 2014 было объявлено, что Python 2.7 будет поддерживаться до 2020 года, и подтверждено, что релиза 2.8 не будет, так как 
предполагается, что пользователи должны переходить на версию 3.4+ при первой же возможности['''


print('dz3 task3 variant1 without using libraries')
marks = '''!()-[]{};?@#$%:'"\,./^&;*_'''
my_str = text.lower()
for x in my_str:
    if x in marks:
        my_str = my_str.replace(x, "")
my_list = my_str.split()
my_dict = {}
for word in my_list:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1
result = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print('Выводим словарь для иллюстрации убывания частоты вхождений')
print(result[:10])
print()


print('dz3 task3 variant2 use libraries')
result = dict(Counter(text.translate(str.maketrans('', '', punctuation)).lower().split()).most_common(10))
print(f'{result.keys() = }')


'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака.'''


BACKPACK = 10

#import math
print()
print('dz3 task 4')
camping_things = {'tent': 3,
                  'pot': .5,
                  'sleeping_bag': 1,
                  'ax': 1.5,
                  'hacksaw': 1.5,
                  'ropes': .5,
                  'knife': .2,
                  'spoon': .1,
                  'mag': .1,
                  'stew': 1,
                  'brot': 2,
                  'mathes': .01,
                  'water': 5,
                  'ather_food': 5,
                  'ball': .4,
                  'map': .1,
                  'sweater': .7,
                  }
number_of_things = len(camping_things)
camping_list = sorted(camping_things.items(), key=lambda x: x[1], reverse=True)
result = []
for i in range(number_of_things):
     list_of_things = []
     weight = 0
     if camping_list[i][1] > BACKPACK:
         continue
     weight += camping_list[i][1]
     list_of_things += [camping_list[i][0]]
     for j in range(i + 1, number_of_things):
         if weight + camping_list[j][1] > BACKPACK:
             continue
         weight += camping_list[j][1]
         list_of_things += [camping_list[j][0]]
     result += [f' weight = {round(weight, 2)}, thingth: '] + [list_of_things]
for i in result:
    print(i)




