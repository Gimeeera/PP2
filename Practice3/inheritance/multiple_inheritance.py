# Умеет летать
class Fly:
    def fly(self):
        print("Летит")


# Умеет плавать
class Swim:
    def swim(self):
        print("Плывет")


# Наследование от двух классов
class Duck(Fly, Swim):
    pass

duck = Duck()
duck.fly()
duck.swim()