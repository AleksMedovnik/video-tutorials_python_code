# Кортеж - неизменяемый список
# tuple

user = ('Alex', 20, 'alex@a.com')
print(user)

user = 'Alex', 20, 'alex@a.com'
print(user)  # ('Alex', 20, 'alex@a.com')

user2 = ('Alex', )
print(user2)  # ('Alex',)

print(user[0])  # Alex
print(user[-1])  # alex@a.com
print(user[:-1])  # ('Alex', 20)

name, age, email = user
print(email)  # alex@a.com

# user[0] = 'John' # 'tuple' object does not support item assignment

print(name in user)  # True
print(21 in user)  # False
for elem in user:
    print(elem)  # 'Alex' 20 'alex@a.com'


print(len(user))  # 3


def sum_elem(a, b):
    return a + b


results = {
    (1, 2): 3,
    (5, 5): 10,
    ('hello', 'world'): 'helloworld'
}

print(results[(1, 2)])  # 3

lst = [1, 2, 3, 4, 5, ]

tpl = tuple(lst)
print(tpl)  # (1, 2, 3, 4, 5)

x, y, z = 10, 20, 30
print(y)  # 20


def get_data(a, b):
    return a + b, a * b


res = get_data(2, 3)
print(res)  # (5, 6)

sum_elem, mul_elem = res[0], res[1]

sum_elem, mul_elem = get_data(2, 3)
print(mul_elem)  # 6
print(sum_elem)  # 5

print(type(res))  # tuple

data = 123,
print(data)  # (123,)

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(numbers[1:-1])  # (2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[1::-1])  # (2, 1)
print(numbers[1:-1:2])  # (2, 4, 6, 8)
print(numbers[:-1:2])  # (1, 3, 5, 7, 9)
print(numbers[::2])  # (1, 3, 5, 7, 9)
print(numbers[::-1])  # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(numbers[1::-1])  # (2, 1)
print(numbers[::-2])  # (10, 8, 6, 4, 2)
