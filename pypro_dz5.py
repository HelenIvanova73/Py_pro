'''Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
 путь, имя файла, расширение файла.'''

def path_find(s: str) -> tuple[str]:
    x = s.rfind('.')
    y = s.rfind('/') + 1
    type_of_file = s[x + 1:]
    name_of_file = s[y: x]
    path = s[: y]
    return (path, name_of_file, type_of_file)


path, name_of_file, type_of_file = path_find('https://gb.ru/lessons/327058/homework/dz5.py')
print(f'{path = }, {name_of_file = }, {type_of_file = }')


''' 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
 премия str с указанием процентов вида “10.25%”.( В результате получаем словарь с именем в качестве ключа и суммой премии
  в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии'''

names = ['Иванов', 'Петров', 'Сидоров', 'Кошкин', 'Мышкин', ]
salaries = [100_000, 120_000, 115_000, 200_000, 90_000, ]
premiums = ['10.25%', '10.20%', '10.35%', '10.25%', '10.22%', ]
premiums = list(map(lambda x: float(x.replace('%', '')), premiums))
my_dict = {name: salary * ((premium) / 100 + 1) for name, salary, premium in zip(names, salaries, premiums)}
for key, value in my_dict.items():
    print(f'{key} {value :.2f}')

''' 3. Создайте функцию генератор чисел Фибоначчи'''

def fib(n: int) -> list[int]:
    n1 = n2 = 1
    result = [n1, n2]
    for _ in range(3, n + 1):
        res = n1 + n2
        result += [res]
        n1 = n2
        n2 = res
    yield result


n = int(input('Ввeдите количество чисел Фибоначчи: '))
print(*fib(n))












14




