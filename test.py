
from dataclasses import dataclass, field


# dataclasses

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name


u = User('Вася', 20)
print(u)


@dataclass
class User:
    name: str
    age: int
    is_student: bool = False  # в конце
    friends: list = field(default_factory=list)


user = User('Вася', 20, True, ['Маша', 'Даша', 'Саша'])
print(user)


@dataclass
class Rectangle:
    width: int
    height: int
    area: int = field(init=0)

    def __post_init__(self):
        self.area = self.width * self.height


rect = Rectangle(30, 20)
print(rect)


print(hash((1, 2, 3)))
print(hash((1, 2, 3)))


#################################################



