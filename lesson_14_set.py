# Множество
# set

# объявление
values = {1, 2, 3, 1, 2, 3}
print(values)  # {1, 2, 3}

s = {2, 1, 4, 6, 8, 5}
print(s)

# print(s[0]) # 'set' object is not subscriptable

s = {}
print(type(s))  # dict

s = set()
print(type(s))  # set

lst = [1, 2, 3, 6, 4]
s = set(lst)
print(s)  # {1, 2, 3, 4, 6}

lst1 = list(s)
print(lst1)  # [1, 2, 3, 4, 6]


# получение элементов
for elem in s:
    print(elem)

print(3 in s)  # True
print(5 in s)  # False

# добавление элемента
s.add(5)
print(s)  # {1, 2, 3, 4, 5, 6}

# удаление элемента
s = {1, 3, 9, 4, 6, 5, 7, 1}
print(s.pop())  # 1
print(s)  # {3, 4, 5, 6, 7, 9}

s.remove(4)
print(s)  # {3, 5, 6, 7, 9}
# s.remove(4) # KeyError: 4

s.discard(4)
s.discard(9)
print(s)  # {3, 5, 6, 7}


def set_uniq_values(lst):
    return list(set(lst))


lst1 = [3, 2, 1, 4, 1, 2, 3]
print(set_uniq_values(lst1))  # [1, 2, 3, 4]


s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 6, 7, 8}

# пересечение
print(s1.intersection(s2))  # {1, 3}

# объединение
s3 = s1.union(s2)
print(s3)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1)  # {1, 2, 3, 4, 5}

# обновление
s1.update(s2)
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# разность
s4 = s3.difference(s2)
print(s4)  # {2, 4, 5}

print(s2)  # {1, 3, 6, 7, 8}
print(s3)  # {1, 2, 3, 4, 5, 6, 7, 8}


'''
Написать функцию get_inner_table, принимающую два множества и возвращающую
список чисел, которые присутствуют в обоих множествах.
Пример:
s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 6, 7, 8}
result = get_inner_table(s1, s2)
print(result) # [1, 3]
'''

def get_inner_table(set1, set2):
    return list(set1.intersection(set2))


s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 6, 7, 8}
result = get_inner_table(s1, s2)
print(result) # [1, 3]