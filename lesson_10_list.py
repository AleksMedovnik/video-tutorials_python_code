# list
from functools import reduce
from random import randint

values = [10, 20, 30, 40, 50, ]


# получение элемента списка
print(values[0])  # 10
print(values[4])  # 50
print(values[-1])  # 50
print(values[-5])  # 10
print(values[1:-1])  # [20, 30, 40]
print(values[1:])  # [20, 30, 40, 50]
print(values[:-1])  # [10, 20, 30, 40]


# изменение списка
values[0] = 100
print(values)  # [100, 20, 30, 40, 50]


# добавление
values.append(60)  # в конец списка
values.insert(0, 10)  # по индексу
values.extend([70, 80, 90])  # в конец списка несколько элементов


# удаление
values.pop()  # последнего элемента
values.pop(1)  # по индексу
values.remove(40)  # по значению

print(values)


def change_values(lst):
    a = int(input('Enter A: '))
    b = int(input('Enter B: '))
    lst.insert(0, a)
    lst.append(b)


# change_values(values)
print(values)


# перебор списка
users = ['Alex', 'Marie', 'Bob', 'John']

for user in users:
    print(f'Hello, {user}')


# количество элементов списка
print(len(values))


alex, marie, bob, john = users
print(john, alex)  # John Alex

print(users)  # ['Alex', 'Marie', 'Bob', 'John']


# фильтрация списка

def filt1(lst):
    new_lst = []
    for elem in lst:
        if elem > 30:
            new_lst.append(elem)
    return new_lst


vls1 = filt1(values)
print(vls1)  # [50, 60, 70, 80]


def filt2(lst):
    new_lst = []
    for elem in lst:
        if elem % 2:
            new_lst.append(elem)
    return new_lst


vls2 = filt2([1, 2, 3, 4, 5])
print(vls2)  # [1, 3, 5]


def filt3(lst):
    new_lst = []
    for elem in lst:
        if len(elem) >= 2:
            new_lst.append(elem)
    return new_lst


vls3 = filt3(['John', 'Marie', 'Li', 'Alex', 'X', 'Y'])
print(vls3)  # ['John', 'Marie', 'Li', 'Alex']


def filt(f, lst):
    new_lst = []
    for elem in lst:
        if f(elem):
            new_lst.append(elem)
    return new_lst


vls1 = filt(lambda elem: elem > 30, values)
print(vls1)  # [50, 60, 70, 80]
print(filt(lambda elem: elem % 2, [1, 2, 3, 4, 5]))  # [1, 3, 5]

vls3 = filt(lambda elem: len(elem) >= 2, [
            'John', 'Marie', 'Li', 'Alex', 'X', 'Y'])
print(vls3)  # ['John', 'Marie', 'Li', 'Alex']


vls1 = list(filter(lambda elem: elem > 30, values))
print(vls1)  # [50, 60, 70, 80]
print(list(filter(lambda elem: elem % 2, [1, 2, 3, 4, 5])))  # [1, 3, 5]

vls3 = list(filter(lambda elem: len(elem) >= 2, [
            'John', 'Marie', 'Li', 'Alex', 'X', 'Y']))
print(vls3)  # ['John', 'Marie', 'Li', 'Alex']


# преобразование списка

vls = [1, 2, 3, 4, 5]


def map1(lst):
    new_lst = []
    for elem in lst:
        new_lst.append(elem * 2)
    return new_lst


vls2 = map1(vls)
print(vls2)  # [2, 4, 6, 8, 10]
print(vls)  # [1, 2, 3, 4, 5]


vls3 = ['1', '2', '3', '4', '5']


def map2(lst):
    new_lst = []
    for elem in lst:
        new_lst.append(int(elem))
    return new_lst


print(map2(vls3))  # [1, 2, 3, 4, 5]
print(map2(['10', '20', '30', '40', '50']))  # [10, 20, 30, 40, 50]


def map_(f, lst):
    new_lst = []
    for elem in lst:
        new_lst.append(f(elem))
    return new_lst


print(map_(int, vls3))  # [1, 2, 3, 4, 5]
print(map_(int, ['10', '20', '30', '40', '50']))  # [10, 20, 30, 40, 50]

vls2 = map_(lambda elem: elem * 2, vls)
print(vls2)  # [2, 4, 6, 8, 10]


vls2 = map(lambda elem: elem * 2, vls)
print(list(vls2))  # [2, 4, 6, 8, 10]

print(list(map(int, vls3)))  # [1, 2, 3, 4, 5]
print(list(map(int, ['10', '20', '30', '40', '50'])))  # [10, 20, 30, 40, 50]


# преобразование строки в список
names = 'alex marie nataly bob'

names_lst = names.split(' ')  # ['alex', 'marie', 'nataly', 'bob']
print(names_lst)

# преобразование списка к строке
names2 = ', '.join(names_lst)  # "alex, marie, nataly, bob"
print(names2)

names = ', '.join(names.split(' '))  # "alex, marie, nataly, bob"

names = ', '.join(names.split(' '))  # "alex, marie, nataly, bob"
print('alex'[0].upper() + 'alex'[1:])


users = 'alex marie nataly bob'

u1 = users.split(' ')
print(u1)  # ['alex', 'marie', 'nataly', 'bob']
u2 = list(map(lambda user: user[0].upper() + user[1:], u1))
print(u2)  # ['Alex', 'Marie', 'Nataly', 'Bob']
u3 = ', '.join(u2)
print(u3)  # Alex, Marie, Nataly, Bob

users = ', '.join(
    map(lambda user: user[0].upper() + user[1:], users.split(' ')))
print(users)  # Alex, Marie, Nataly, Bob


emails = ['alex.mail.com', 'marie@mail.com',
          'bob@mail.com', 'vasya@mail.com', 'alex.mail.com']

# количество вхождений элемента
print(emails.count('alex.mail.com'))  # 2

# получить индекс элемента
print(emails.index('marie@mail.com'))  # 1
print(emails.index('alex.mail.com'))  # 0

# поиск элемента
print('bob@mail.com' in emails)  # True
print('bob@mail.com' not in emails)  # False
print('nataly@mail.com' not in emails)  # True

# фильтруем emails
print('@' in 'alex.mail.com')  # False
print('@' in 'marie@mail.com')  # True

emails = list(filter(lambda email: '@' in email, emails))
print(emails)  # ['marie@mail.com', 'bob@mail.com', 'vasya@mail.com']


# генератор списка

lst = [i * 2 for i in range(2, 11) if i % 2]
print(lst)  # [6, 10, 14, 18]

lst2 = [1, -2, -3, 4, 0, 5, -6, 7, 8, -9, 10]
lst3 = [i * 2 for i in lst2 if i > 0]
print(lst3)  # [2, 8, 10, 14, 16, 20]


# lst4 = []
# for i in range(3):
#     lst4.append(int(input('Enter the number: ')))

# lst4 = [int(input('Enter the number: ')) for i in range(3)]
# print(lst4)


lst = [[i, j] for i in [1, 2, 3] for j in range(3)]
print(lst)


def build_table(lst, cols):
    return [lst[i:i+cols] for i in range(0, len(lst), cols)]


# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
print(build_table([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], randint(2, 4)))

# копирование объекта по ссылке
lst = [1, 2, 3]
lst2 = lst

print(lst == lst2)  # True
print(lst is lst2)  # True

lst2.append(4)
print(lst)  # [1, 2, 3, 4]

lst3 = [*lst]  # [1, 2, 3, 4]
print(lst3)
print(lst3 is lst)  # False

lst4 = lst
print(lst4)  # [1, 2, 3, 4]

lst = [10, 20, 30]
print(lst4)  # [1, 2, 3, 4]

print(lst is lst4)  # False

score = 100
message = 'Ты лучший!' if score >= 80 else 'Учись играть, нубик!'
print(message)

vls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def reverse_lst(lst):
    new_lst = []
    for elem in lst:
        new_lst.insert(0, elem)
    return new_lst


print(reverse_lst(vls))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(vls)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(reversed(vls)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(vls)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


vls.reverse()
print(vls)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

vls2 = [1, 2, 3, 4, 5]
print(sum(vls2))  # 15

sum_numb = reduce(lambda a, b: a + b, vls2)
print(sum_numb)  # 15

print(reduce(lambda a, b: a * b, vls2))  # 120


# сортировка

lst1 = [1, 3, 2, 6, 5, 4, 9, 7, 8]

lst1.sort()
print(lst1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# по возрастанию
lst2 = [1, 3, 2, 4, 6, 5]
lst3 = sorted(lst2)
print(lst3) # [1, 2, 3, 4, 5, 6]
print(lst2) # [1, 3, 2, 4, 6, 5]

# по убыванию
lst4 = sorted(lst2, reverse=True)
print(lst4) # [6, 5, 4, 3, 2, 1]


users = [
    {'id': 1, 'name': 'Vasya', 'age': 25},
    {'id': 2, 'name': 'John', 'age': 16},
    {'id': 3, 'name': 'Bob', 'age': 35},
    {'id': 4, 'name': 'Alex', 'age': 18},
]

print(sorted(users, key=lambda user: user['age']))
print(sorted(users, key=lambda user: user['id'], reverse=True))