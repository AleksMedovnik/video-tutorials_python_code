user_name = 'Вася'  # глобальная переменная

# объявление функции


def say_hello():
    user_name = 'John'  # локальная переменная
    print(f'Hello, {user_name}!')


# вызов
say_hello()  # Hello, John!
say_hello()  # Hello, John!
say_hello()  # Hello, John!

print(user_name)  # Вася


# параметры функции

def say_hi(user_name):
    print(f'Hello, {user_name}!')


say_hi('Петя')  # Hello, Петя!
say_hi('Alex')  # Hello, Alex!
say_hi(user_name)  # Hello, Вася!


# изменение глобальной переменной

def edit_user_name(name):
    global user_name
    user_name = name


edit_user_name('Alex')
print(user_name)  # Alex
edit_user_name('Петя')
print(user_name)  # Петя
edit_user_name('Вася')
print(user_name)  # Вася


def display_info(user_name, user_age):
    print(f'Ваше имя: {user_name}; возраст: {user_age}')


display_info('Вася', 18)  # Ваше имя: Вася; возраст: 18


valid_login = 'admin'
valid_password = '123xz'


def sign_in():
    user_login = input('Введите логин: ')
    if user_login == valid_login:
        user_password = input('Введите пароль: ')
        if user_password == valid_password:
            print('Вы вошли в систему!')
        else:
            print('Пароль неверный')
    else:
        print('Login неверный')


# sign_in()


# возврат значения

def calc_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


calc_factorial(3)  # 6
calc_factorial(11)  # 39916800


# name = input('Введите имя: ')
# print(f'Ваше имя: {name}')

# a = print('Hello') # Hello
# print(a) # None

def sum_args(a, b):
    return a + b


result = sum_args(1, 2)
print(result ** 2)


fact = calc_factorial(11)
print(fact)  # 39916800


def sq_number(x):
    return x ** 2


result = sq_number(5)
print(result)  # 25


def check_target():
    for i in range(3):
        for j in range(3):
            target = int(input(f'TR: {i}; TD: {j}: '))
            if target == 10:
                print("Цель поражена!")
                return
    print('Ты - лузер!')


# check_target()


# аргументы по умолчанию

def say_welcome(user_name='Guest'):
    print(f'Welcome, {user_name}!')


say_welcome('Alex')  # Welcome, Alex!
say_welcome()  # Welcome, Guest!


# именованные аргументы

def display_data(a=0, b=1, c=2):
    print(f'A: {a}; B: {b}; C: {c}')


display_data(1, 2, 3)  # A: 1; B: 2; C: 3
display_data()  # A: 0; B: 1; C: 2
display_data(5, 6)  # A: 5; B: 6; C: 2
display_data(c=10)  # A: 0; B: 1; C: 10
display_data(20, c=10)  # A: 20; B: 1; C: 10


def mul(a=1, b=1, c=1):
    return a * b * c


print(mul())  # 1
print(mul(2, 3, 4))  # 24
print(mul(2, 3))  # 6
print(mul(2, c=5))  # 10


# lambda
def show_massage(): return print('Hello!')


show_massage()  # Hello!


def double(x): return x * 2


print(double(5))  # 10


def multiplay(a, b): return a * b


print(multiplay(5, 3))  # 15


def wrapper(f):
    print('Какой-то очень важный код!')
    f()


wrapper(say_hello)
wrapper(lambda: print('Goodbye'))


# замыкание
x = 1


def s(a): return a + x


print(s(1))  # 2


def f():
    print(x)
    return x


def f2():
    x = 0
    return f()


f2()  # 1


def increment():
    i = 0

    def count():
        nonlocal i
        i += 1
        return i
    return count


counter1 = increment()
print(counter1)

print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3


print(counter1())  # 4


def sum_args(a):
    print(a)

    def f(b):
        nonlocal a
        a += b
        print(a)
        return f
    return f


sum_args(1)(2)(3)(4)(5)  # 1 3 6

# f(5) # 1 3 6 10 15

counter2 = increment()
print(counter2())  # 1
print(counter1())  # 5


# кортеж аргументов *args
lst = [1, 2, 3]
lst2 = [*lst]
print(lst == lst2)  # True
print(lst is lst2)  # False


def f(*args):
    print(args)  # (1, 2, 3)
    print(type(args))  # tuple
    print(args[0])  # 1
    print(*args)  # 1 2 3
    print(sum(args))  # 6
    for i in args:
        print(i)


f(1, 2, 3)
f(1, 2, 3, 4, 5)


# словарь именованных параметров **kwargs
def f(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2}
    print(type(kwargs))  # dict


f(a=1, b=2)


def display_info(**kwargs):
    print(f"Your name: {kwargs['name']}, your age: {kwargs['age']}")
    print(kwargs)


display_info(name='Alex', age=22, id=122)  # Your name: Alex, your age: 22
display_info(name='Vasya', age=18, id=123)  # Your name: Vasya, your age: 18


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(1, 2, 3)
f(a=1, b=2)
f()

# декоратор
def show_welcome(f):
    def wrapper(*args, **kwargs):
        print("Hello!")
        f(*args, **kwargs)
        print('Good bye!')
    return wrapper


@show_welcome  # calculator = show_welcome(calculator)
def calculator():
    print(eval(input('Введите умное математическое выражение: ')))

# calculator()


@show_welcome  # check_target = show_welcome(check_target)
def check_target():
    for i in range(3):
        for j in range(3):
            target = int(input(f'TR: {i}; TD: {j}: '))
            if target == 10:
                print("Цель поражена!")
                return
    print('Ты - лузер!')

# check_target()


@show_welcome
def sum_args(a, b):
    print(a + b)


# show_welcome.<locals>.wrapper() takes 0 positional arguments but 2 were given
sum_args(1, 2)


# dic = {'a': 1, 'b': 2}
# print((1, 2, 3) + tuple(dic.items()))


def cache(func):
    # кеш предыдущих вызовов
    cache_calls = {}

    def wrapper(*args, **kwargs):
        tuple_args = args + tuple(kwargs.items())
        if tuple_args in cache_calls:
            return cache_calls[tuple_args]
        result = func(*args, **kwargs)
        cache_calls[tuple_args] = result
        return result

    return wrapper


@cache
def sum_all(a=1, b=2, c=3):
    # тяжелый код в качестве примера
    for i in range(10_000_000):
        i += a + b + c
    return i


# print(sum_all(10, c=30))  # 10000041
# print(sum_all(10, c=30))
# print(sum_all(10, c=30))
# print(sum_all(10, c=30))
# print(sum_all(10, c=30))

# print(sum_all(10, 5, c=30))  # 10000044
# print(sum_all(10, 5, c=30))
# print(sum_all(10, 5, c=30))
# print(sum_all(10, 5, c=30))


# рекурсия
def f(n):
    print(n)
    f(n + 1)

# f(1) # 996 # maximum recursion depth exceeded while calling a Python object


def sum_numbers_given(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result

print(sum_numbers_given(5)) # 15

print(sum_numbers_given(0)) # 0
print(sum_numbers_given(1)) # 1
print(sum_numbers_given(-10)) # 0

n = 0
print(sum_numbers_given(n) == n) # True

n = 1
print(sum_numbers_given(n) == n) # True

n = 300
print(sum_numbers_given(n) == n + sum_numbers_given(n - 1)) # True


def sum_numbers_given_rec(n):
    return n if n in (0, 1) else n + sum_numbers_given_rec(n - 1)

print(sum_numbers_given(5)) # 15
print(sum_numbers_given_rec(5)) # 15

print(sum_numbers_given(5000)) # 12502500
# print(sum_numbers_given_rec(1000)) # maximum recursion depth exceeded in comparison

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(3)) # 6
print(factorial(5)) # 120
print(factorial(11)) # 39916800

def factorial_rec(n):
    return n if n in (1, 2) else n * factorial_rec(n - 1)

print(factorial_rec(3)) # 6
print(factorial_rec(5)) # 120
print(factorial_rec(11)) # 39916800



def f1():
    print(1)

def f2():
    print(2)

def f3():
    print(3)

stack = []

stack.append(f1)
f1()
print(stack)
stack.pop()

stack.append(f2)
f2()
print(stack)
stack.pop()

stack.append(f3)
f3()
print(stack)
stack.pop()

print(stack)

# stack.append(f)
# f(1)
# print(stack)
# stack.pop()

# []