class User:
    # функция-конструктор объекта
    def __init__(self, country):
        # приватные атрибуты
        self.__name = '' 
        self.__age = 0
        self.country = country

    # геттер
    @property
    def name(self): # get_name(self)
        return self.__name

    # сеттер
    # определяется только после геттера
    @name.setter
    def name(self, name): # set_name(self, name)
        if len(name) < 2:
            print('Имя не должно быть короче 2-х символов')
        else:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 6 < age < 120:
            self.__age = age
        else:
            print('Введите правильный возраст!')

    def say_hello(self):
        print('Hello!')

    def display_info(self):
        print(f'Имя пользователя: {self.__name}')
        print(f'Возраст пользователя: {self.__age}')
        print(f'Страна пользователя: {self.country}')


# использование класса
user1 = User('Египет') # вызывается конструктор
user1.name = 'Bob'
print(user1.name) # Bob
user1.age = 30
print(user1.age) # 30
user1.age = -30 # Введите правильный возраст!
user1.age = 300# Введите правильный возраст!
print(user1.age) # 30

user1.name = 'X' # Имя не должно быть короче 2-х символов
print(user1.name) # Bob
print(user1.country)
user1.say_hello()
user1.display_info()

# наследование класса
class Student(User):
    def __init__(self, country, faculty):
        super().__init__(country)
        self.faculty = faculty

    def to_study(self):
        print('Студент учится!')

    # переопределение метода суперкласса
    def say_hello(self):
        print('Hello, student!')

    # расширение метода суперкласса
    def display_info(self):
        super().display_info()
        print(f'Факультет студента: {self.faculty}')


student = Student('Китай', 'Медицина')
student.name = 'Ли'
student.age = -100 # Введите правильный возраст!
student.age = 19
student.say_hello()
student.to_study()
student.say_hello()
print(student.faculty)
student.display_info()

# множественное наследование классов
class APIView:
    def get(self):
        print('Ресурс получен!')

    def post(self):
        print('Ресурс добавлен!')

    def put(self):
        print('Ресурс обновлен!')

    def delete(self):
        print('Ресурс удален!')


class ListAPIView(APIView):
    def get(self):
        print('Ресурс получен сейчас!')


class ListCreateAPIView(APIView):
    def get(self):
        print('Ресурс получен успешно!')

    def post(self):
        print('Ресурс добавлен успешно!')


class ModelAPIView(ListAPIView, ListCreateAPIView):
    def put(self):
        print('Ресурс изменен!')


model = ModelAPIView()
model.get() # Ресурс получен сейчас!
model.post() # Ресурс добавлен успешно!
model.put() # Ресурс изменен!
model.delete() # Ресурс удален!


# Полиморфизм

class SuperHero:
    def display_info(self):
        print('Я - супер-герой!')


class Bat(SuperHero):
    def use_super_power(self):
        print('Bat летает!')


class Spider(SuperHero):
    def use_super_power(self):
        print('Spider ползает по стенам!')


class Reptile(SuperHero):
    def use_super_power(self):
        print('Reptile плавает и кусается!')


bat = Bat()
spider = Spider()
reptile = Reptile()

bat.display_info()
spider.display_info()
reptile.display_info()

bat.use_super_power()
spider.use_super_power()
reptile.use_super_power()


class Square:
    # атрибут класса Square
    total_instances = 0

    def __init__(self, width):
        Square.total_instances += 1
        self.width = width

    # метод класса
    @classmethod
    def count_instances(cls):
        return cls.total_instances

    # метод экземпляра класса
    def area(self):
        return self.width ** 2


class Rect(Square):
    # атрибут класса Rect
    total_instances = 0

    def __init__(self, width, height):
        super().__init__(width)
        Rect.total_instances += 1
        self.height = height

    # переопределение метода экземпляра класса
    def area(self):
        return self.width * self.height

    # статический метод
    @staticmethod
    def get_perimeter_rect(width, height):
        return (width + height) * 2


square1 = Square(50)
rect1 = Rect(100, 50)

print(square1.area()) # 2500
print(rect1.area()) # 5000

print(Square.count_instances()) # 2
print(Rect.count_instances()) # 1
print(rect1.count_instances()) # 1

print(Rect.get_perimeter_rect(30, 40)) # 140



class Rect:
    total_instances = 0

    def __init__(self, width, height):
        Rect.total_instances += 1
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    # метод класса
    @classmethod
    def count_instances(cls):
        return cls.total_instances


class Square(Rect):
    total_instances = 0

    def __init__(self, width):
        super().__init__(width, width)
        Square.total_instances += 1


sqare = Square(150)
print(sqare.perimeter())