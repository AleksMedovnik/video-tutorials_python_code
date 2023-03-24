import random 
from random import randint


def sum_args(a, b):
    """Функция принимает 2 целых числа и возвращает их сумму.
    
    Аргументы: a, b - целые числа.

    Если аргументы не являются целыми числами, то функция возвращает строку c 
    сообщением о неверном типе аргументов.
    
    """

    if type(a) == type(b) == int:
        return a + b
    
    return 'Аргументы должны быть целыми числами!'


print(sum_args(1, 3))
print(sum_args(1, '10'))

print(random.__doc__)
print(sum_args.__doc__)
