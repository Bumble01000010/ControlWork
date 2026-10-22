# class Person:
#     def __init__(self, age = None):
#         self.__age = age
#
#     def set_age(self, ageArgument):
#         if ageArgument <= 0:
#             raise ValueError('Возраст должен быть больше нуля')
#         self.__age = ageArgument
#
#     def get_age(self):
#         return self.__age
#
#
# p = Person()
# p.set_age(25)
# print(p.get_age())
# p.set_age(-5)

#_______________________________________________________________________________________________________________________

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'I am an animal'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Woof*'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Meow*'

dog = Dog('Buddy')
cat = Cat('Kitty')
print(dog.name, dog.speak())
print(cat.name, cat.speak())

#_______________________________________________________________________________________________________________________

class Vehicle:
    def move(self):
        return 'Vehicle is moving'

class Car(Vehicle):

    def move(self):
        return 'Car is driving'

class Bicycle(Vehicle):

    def move(self):
        return 'Bicycle is pedaling'

car = Car()
bike = Bicycle()
print(car.move())
print(bike.move())

#_______________________________________________________________________________________________________________________

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width / 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

rect = Rectangle(10, 5)
circle = Circle(7)
print(rect.area())
print(circle.area())