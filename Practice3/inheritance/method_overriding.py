# Родительский класс
class Animal:
    def make_sound(self):
        print("Какой-то звук")


# Переопределение метода
class Dog(Animal):
    def make_sound(self):
        print("Гав-гав")

dog = Dog()
dog.make_sound()