# Родительский класс
class Animal:
    def eat(self):
        print("Животное ест")


# Дочерний класс
class Dog(Animal):
    pass

dog = Dog()
dog.eat()