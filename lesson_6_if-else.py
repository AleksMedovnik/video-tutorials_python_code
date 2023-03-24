from random import randint
 
'''
score = int(input('Score: '))

if score < 30:
    print('Учись играть, нубик!')
elif score < 50:
    print('Ты играешь неплохо!')
elif score < 80:
    print('Ты играешь хорошо!')
elif score < 100:
    print('Ты играешь отлично!')
else:
    print('Ты - лучший!')
'''

##################################################################

'''
NORMAL_TEMPERATURE = 36.6

user_temperature = float(input('Введите температуру вашего тела: '))


if user_temperature > NORMAL_TEMPERATURE:
    print(f'Температура вашего тела превышает норму на {round(user_temperature - NORMAL_TEMPERATURE, 1)}')
elif user_temperature < NORMAL_TEMPERATURE:
    print(f'Температура вашего тела ниже нормы на {round(NORMAL_TEMPERATURE - user_temperature, 1)}')
else:
    print('Вы здоровы!')
'''

# a = int(input('A: '))
# b = int(input('B: '))

# if a < b:
#     print(a)
# else:
#     print(b)


# valid_login = 'admin'
# valid_password = '123xz'

# user_login = input('Введите логин: ')
# if user_login == valid_login:
#     user_password = input('Введите пароль: ')
#     if user_password == valid_password:
#         print('Вы вошли в систему!')
#     else:
#         print('Пароль неверный')
# else:
#     print('Login неверный')


print('Я - бот! Я загадаю число от 1 до 5, а ты попробуй его отгадать!')
value = randint(1, 5)
result = int(input('Твой ответ: '))

if result == value:
    print('Ты угадал! Молодец!')
else:
    print(f'Ты не угадал. Я загадал число {value}')
