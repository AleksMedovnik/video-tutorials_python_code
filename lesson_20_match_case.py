direction = input('Enter direction: ').lower()

if direction == 'left':
    print('Я иду налево!')
elif direction == 'right':
    print('Я иду направо!')
elif direction == 'up' or direction == 'top':
    print('Я ползу вверх!')
elif direction == 'down' or direction == 'bottom':
    print('Я спускаюсь вниз!')
else:
    print('Выбрано неверное направление')




def get_user_names(users: list[dict]) -> list[str]:
    return list(map(lambda user: user['name'], users))


users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

print(get_user_names(users))  # ['Vasya', 'Bob', 'Alex']
print(get_user_names([])) # None
print(get_user_names('hello')) # None