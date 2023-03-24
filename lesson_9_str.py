message = 'hello'

print(message[0])  # h
print(message[4])  # o
print(message[-1])  # o
print(message[-5])  # h
print(message[1:-1])  # ell
print(message[1:])  # ello
print(message[:-1])  # hell

# phrase = input('Enter your message: ')
# print(phrase[-1] + phrase[1:-1] + phrase[0])


# message[0] = 'X'  # 'str' object does not support item assignment

message = 'World'
print(message)  # World


# преобразование к верхнему регистру
print('hello'.upper()) # HELLO

# преобразование к нижнему регистру
print('HELLO'.lower()) # hello

message = 'hello'
print(message[0].upper() + message[1:])