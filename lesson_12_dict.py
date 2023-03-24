# словарь

values = {1: 10, 2: 20, 3: 30, }

# получение значения
print(values[1])  # 10
print(type(values))  # dict
print(len(values))  # 3

user = {
    'name': 'Vasya',
    'age': 20,
    'isStudent': False
}

print(user['name'])  # Vasya


# измение значения
user['isStudent'] = True
print(user)  # {'name': 'Vasya', 'age': 20, 'isStudent': True}

# добавление значения
user['country'] = 'Russia'
# {'name': 'Vasya', 'age': 20, 'isStudent': True, 'country': 'Russia'}
print(user)

# удаление значения
del user['country']
print(user)  # {'name': 'Vasya', 'age': 20, 'isStudent': True}

salaries = {
    'Bob': 2000,
    'John': 2500,
    'Marie': 3000
}

for user_name in salaries:
    print(user_name)  # key

for user_name in salaries:
    print(salaries[user_name])  # value

sum_salaries = 0
for user_name in salaries:
    sum_salaries += salaries[user_name]

print(sum_salaries)  # 7500


# список ключей
keys = salaries.keys()
print(list(keys))  # ['Bob', 'John', 'Marie']


# список значений
values = salaries.values()
print(list(values))  # [2000, 2500, 3000]

# сумма
print(sum(values))  # 7500


phonebook = {
    'Bob': '+123 400 500',
    'John': '+123 400 795',
    'Marie': '+123 400 456',
}

# name = input('Enter name: ')
# print(phonebook[name])


student = {'faculty': 'Medicine', 'course': 3}

user.update(student)
# {'name': 'Vasya', 'age': 20, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}
print(user)

print(student)  # {'faculty': 'Medicine', 'course': 3}

users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]


def get_user_names(users):
    return list(map(lambda user: user['name'], users))


print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']


bob_tel = phonebook.get('Bob', None)
print(bob_tel)  # +123 400 500

alex_tel = phonebook.get('Alex', None)
print(alex_tel)  # None

print(users)

users2 = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Alex', 'age': 25},
]


def get_aver_age(users):
    sum_ages = 0
    for user in users:
        age = user.get('age', None)
        if not age:
            return 'Возраст пользователя отсутствует'
        sum_ages += age
    return sum_ages / len(users)


aver_age = get_aver_age(users)
print(aver_age)  # 22.0

aver_age = get_aver_age(users2)
print(aver_age)  # Возраст пользователя отсутствует


user2 = user
# {'name': 'Vasya', 'age': 20, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}
print(user)

print(user2 is user)  # True
user2['age'] += 1
print(user['age'])  # 21

# {'name': 'Vasya', 'age': 20, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}
user3 = {**user}
print(user3 is user)  # False
print(user3 == user)  # True


# Ключом словаря может быть любой неизменяемый объект