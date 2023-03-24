def say_hello() -> None:
    print('Hello!')


def calc_factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def mul(a: int = 1, b: int = 1, c: int = 1) -> int:
    return a * b * c


def get_user_names(users: list[dict]) -> list[str]:
    return list(map(lambda user: user['name'], users))

users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']