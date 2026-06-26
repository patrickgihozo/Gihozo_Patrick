#Abstraction hides implementation information by showing only essential things.

#syntax:from abc import ABC , abstractMethod

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")


class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")


dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()