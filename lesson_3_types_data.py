# Типы данных

# 1. int - целое число
x = 1
a = -123

# 2. float - число с плавающей точкой
z = 1.5

# 3. bool - логический тип
check = z > x
print(check)  # True

# 4. str - строка
message = 'Hello'
phrase = "World"
print("I'm happy")

message = 'Hello\nWorld'
print(message)

message = """ Hello
World!!!
"""
print(message)

# 5. None
print(type(None))  # NoneType


print(type('100'))  # str
print(type(123 < 4566))  # bool
print(type("123 < 4566"))  # str
print(type("True")) # str
print(type(True)) # bool
print(type(1.5 + 10)) # float