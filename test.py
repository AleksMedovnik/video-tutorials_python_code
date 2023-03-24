# direction = input('Enter direction: ')

# match direction.lower():
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
            raise Exception('Ошибка при передаче параметров!')


users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']
# print(get_user_names([]))
# print(get_user_names('hello'))


def sigh_up(user_data):
    match user_data:
        case str(name), int(age), bool(experience):
            print(f"""
                Регистрация нового пользователя: 
                Имя: {name}
                Возраст: {age}
                Наличие опыта: {experience}
            """)
        case _:
            print(f'Неверная передача данных!')


sigh_up(('Alex', '39', True, 15))
sigh_up(('Alex', 39, True))


def sigh_up(user_data):
    match user_data:
        case {'name': str(user_name), 'age': int(user_age)}:
            print(f"""
                Регистрация нового пользователя: 
                Имя: {user_name}
                Возраст: {user_age}
            """)
        case _:
            print(f'Неверная передача данных!')


sigh_up({'name': 'Alex', 'age': 39})
sigh_up({'name': 'Alex', 'age': '39'})
