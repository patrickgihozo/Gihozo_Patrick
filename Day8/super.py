#Super() function is used  to call the parent class constructor or methods.

class Animal:
    def __init__(self,name):
        self.name = name
        
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Max","Uganda shepherd")
print(f"{dog.name}, {dog.breed}")
        