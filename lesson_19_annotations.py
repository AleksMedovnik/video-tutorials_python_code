def say_hello() -> None:
    print('Hello!')


def calc_factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def mul(a: int = 1, b: int = 1, c: int = 1) -> int:
    return a * b * c


"""
Написать функцию get_user_names, принимающую список с пользователями и 
возвращающую список с именами пользователей.

users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']

Если в функцию передать не список, а какой-либо другой тип, то должна выбрасываться
ошибка с сообщением "Неверная передача данных"

print(get_user_names('hello')) # Error

Функция должна использовать аннотацию типов и быть задокументирована

При вызове функции сделать обработку ошибок
"""

def get_user_names(users: list[dict]) -> list[str]:
    if type(users) == list:
        return list(map(lambda user: user['name'], users))
    raise Exception('Неверная передача данных') 


users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

print(mul('hello', 2))

print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']


