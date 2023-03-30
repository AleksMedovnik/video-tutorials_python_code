# print(1 + 2 # SyntaxError
# print(int("Hello")) # ValueError
# print("10" + 10) # TypeError
# print(x) # NameError
# print(1 / 0) # ZeroDivisionError

try:
    print('Подключились к ресурсу')
    # print(x)
    print(2)
except ZeroDivisionError:
    print('На 0 делить нельзя!')
except ValueError:
    print('Ошибка при преобразовании!')
except Exception as e:
    print(e)
else:
    print('Операция прошла успешно!')
finally:
    print('Выход из системы')


class User:
    def __init__(self, name):
        if len(name) < 2:
            raise Exception("Имя слишком короткое!")
        self.name = name


try:
    jack = User('Jack')
    print(jack.name) # Jack
    x = User('X') # Exception: Имя слишком короткое!
except Exception as e:
    print(e)


