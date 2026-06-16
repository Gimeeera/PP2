# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name

# Использование super()
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog("Бобик")
print(dog.name)