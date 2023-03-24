# Логические операторы

print(True or False)  # True
print(False or True)  # True
print(1 or 0)  # 1
print(1 or 2 or 3) # 1
print(True or hahaha)  # True
print(None or False or 0)  # 0

print(False and True) # False
print(1 and 0) # 0
print(0 and None and False) # 0
print(0 and hahaha)  # 0
print(-1 and 2 and 3) # 3

print(1 > 0 and 10 < 100) # True
print(1 > 0 or 5 > 10) # True

print(1 > 0 or None and '0')  # True



#############################################################


'''
Пользователь вводит 3 числа. 
Вывести True, если данные числа могут являться сторонами треугольника.
'''


# 5 + 5 or None and 1 > 0 # 10
# 17 % 3 and -1000 and 2 ** 3  # 8
# '0' or 0 and 123  # '0'



'''
Координаты цели: 
X: 100
Y: 150
Z: 50

Пользователь вводит координаты. Вывести True, если цель поражена
'''

# x = int(input('Enter X: '))
# y = int(input('Enter Y: '))
# z = int(input('Enter Z: '))

# print(x == 100 and y == 150 and z == 50)


'''
Пользователь вводит 3 числа. 
Вывести True, если данные числа могут являться сторонами треугольника.
'''

# a = int(input('Enter A: '))
# b = int(input('Enter B: '))
# c = int(input('Enter C: '))

# print(a + b > c and a + c > b and b + c > a)



'''
Наш штаб находится в координатах между 50 и 100: 
Пользователь вводит координаты. Вывести True, если штаб не поражен
'''
# target = int(input('Enter coords: '))
# print(target < 50 or target > 100)
