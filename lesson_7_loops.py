from random import randint

# i = 0

# while i < 5:
#     print(i)  # 0, 1, 2, 3, 4
#     i += 1  # i = i + 1 


# while True:
#     password = input('Enter your password: ')
#     if password == '123cz':
#         print('Welcome!')
#         break


# while True:
#     print('Я - бот! Я загадаю число от 1 до 5, а ты попробуй его отгадать!')
#     value = randint(1, 5)
#     result = int(input('Твой ответ: '))

#     if result == value:
#         print('Ты угадал! Молодец!')
#     else:
#         print(f'Ты не угадал. Я загадал число {value}')


# for i in range(5):
#     print('Hello')

# for i in range(5):
#     print(i)  # 0, 1, 2, 3, 4

# for i in range(3, 9):
#     print(i)  # 3 - 8

# for i in range(1, 10, 2):
#     print(i)  # 1, 3, 5, 7, 9

# for i in range(10, 0, -1):
#     print(i)  


# a = int(input('Enter A: '))
# b = int(input('Enter B: '))


# if a == b:
#     print(a)
# else:
#     if a < b:
#         step = 1
#     else:
#         step = -1
#     for i in range(a, b + step, step):
#             print(i) 


# value = int(input('Введите число: '))
# print('Hello\n' * value)


# valid_password = '123xz'

# for i in range(5):
#     user_password = input('Введите пароль: ')
#     if user_password == valid_password:
#         print('Вы вошли на сайт!')
#         break
# else:   
#     print('Ваш аккаунт заблокирован!')


# for i in range(5):
#     print('Я - бот! Я загадаю число от 1 до 5, а ты попробуй его отгадать!')
#     value = randint(1, 5)
#     result = int(input('Твой ответ: '))

#     if result == value:
#         print('Ты угадал! Молодец!')
#     else:
#         print(f'Ты не угадал. Я загадал число {value}')


# r = range(3, 50, 3)
# for i in r:
#     if i % 2:
#         print(i)  


# n = int(input('Enter number: '))
# result = 0
# for i in range(1, n + 1):
#     result += i

# print(result)

# 5! == 5 * 4 * 3 * 2 * 1


# factorial
# n = int(input('Enter number: '))

# result = 1
# for i in range(2, n + 1):
#     result *= i

# print(result)


# continue
# r = range(3, 50, 3)
# for i in r:
#     if i % 2 == 0:
#         continue
#     print(i)  


check_target = False
for i in range(3):
    for j in range(3):
        target = int(input(f'TR: {i}; TD: {j}: '))
        if target == 10:
            check_target = True
            print("Цель поражена!")
            break 
    if check_target:
        break
else:
    print('Ты - лузер!')