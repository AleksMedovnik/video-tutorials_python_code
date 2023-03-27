# direction = input('Введите направление движения: ').lower()

# match direction:
#     case 'left':
#         print('Я иду налево!')
#     case 'right':
#         print('Я иду направо!')
#     case 'up' | 'top':
#         print('Я ползу вверх!')
#     case 'down' | 'bottom':
#         print('Я спускаюсь вниз!')
#     case _:
#         print('Выбрано неверное направление')


def get_user_names(users: list[dict]) -> list[str]:
    match users:
        case list() if len(users):
            return list(map(lambda user: user['name'], users))
        case _:
            return "Ошибка при передаче данных"


users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']
print(get_user_names([])) # Ошибка при передаче данных
print(get_user_names('hello')) # Ошибка при передаче данных


def sigh_up(user_data: tuple) -> None:
    match user_data:
        case str(name), int(age), bool(expirience):
            print(f"""
                Регистрация нового пользователя: 
                Имя: {name}
                Возраст: {age}
                Наличие опыта: {expirience}
            """)
        case _:
            raise Exception('Ошибка при передаче данных')


# sigh_up(('Alex', 39, True))
# sigh_up(('Alex', '39', 123))
# sigh_up(('Alex', 39))


def sigh_up(user: dict) -> None:
    match user:
        case {'name': str(user_name), 'age': int(user_age)}:
            print(f"""
                Регистрация нового пользователя: 
                Имя: {user_name}
                Возраст: {user_age}
            """)
        case _:
            raise Exception('Ошибка при передаче данных')


# sigh_up({'name': 'Alex', 'age': 39})
# sigh_up({'name': 'Alex', 'age': '39'})
