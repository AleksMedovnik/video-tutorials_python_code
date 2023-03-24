import sys
from itertools import count

lst = [1, 2, 3, 4, 5]

for i in lst:
    print(i)

for i in lst:
    print(i)

m = map(lambda elem: elem * 2, lst)
print(m)  # <map object at 0x000001A7ECF90250>
# print(list(m)) # [2, 4, 6, 8, 10]
# print(list(m)) # []

# for i in m:
#     print(i)

# for i in m:
#     print(i)

# print(list(m)) # []

r = range(10_000_000_000)
print(r[1000])  # 1000
print(r[1])  # 1

# l = list(r) # MemoryError
print(r)  # range(0, 10000000000)


print(next(m))  # 2
print(next(m))  # 4
print(next(m))  # 6
print(next(m))  # 8
print(next(m))  # 10
# print(next(m)) # StopIteration

print(m == iter(m))  # True

it = iter([1, 2, 3])
print(it == iter(it))  # True

g = (i for i in range(10))
print(g)  # <generator object <genexpr> at 0x000001E1DC9420A0>

print(g == iter(g))  # True


print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 152 (бит)

it = iter(range(10_000_000_000))
print(sys.getsizeof(it))  # 48

print(sys.getsizeof(r))  # 48

print(r == iter(r))  # False


# fibonacci
# 0 1 1 2 3 5 8

class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


fibonacci = Fibonacci()
# print(next(fibonacci))  # 0
# print(next(fibonacci))  # 1
# print(next(fibonacci))  # 1
# print(next(fibonacci))  # 2

# print(fibonacci == iter(fibonacci)) # True

# for i in fibonacci:
#     print(i)
#     if i > 100:
#         break


# factorial
# 1 2 3 4  5  6
# 1 2 6 24 120

class Factorial:
    def __init__(self):
        self.elem = self.value = 1

    def __next__(self):
        self.value *= self.elem
        self.elem += 1
        return self.value

    def __iter__(self):
        return self


factorial = Factorial()
# print(next(factorial))  # 1
# print(next(factorial))  # 2
# print(next(factorial))  # 6

# print(factorial == iter(factorial)) # True

# for i in factorial:
#     print(i)
#     if i > 100:
#         break


counter = count(5, 10)

# print(next(counter)) # 5
# print(next(counter)) # 15

# for i in counter:
#     if i > 100:
#         break
#     print(i)


def infinite_sequence_number(prev, step):
    elem = prev
    while True:
        yield elem
        elem += step


sequence = infinite_sequence_number(5, 10)

# print(sequence == iter(sequence)) # True
# print(type(sequence)) # <class 'generator'>

# print(next(sequence)) # 0
# print(next(sequence)) # 1

# for i in sequence:
#     if i > 100:
#         break
#     print(i)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()

# print(fib == iter(fib)) # True
# print(type(fib)) # <class 'generator'>

# print(next(fib)) # 0
# print(next(fib)) # 1

# for i in fib:
#     if i > 100:
#         break
#     print(i)


def factorial():
    elem = value = 1
    while True:
        yield value
        value *= elem
        elem += 1

factor = factorial()

for i in factor:
    if i > 1000:
        break
    print(i)