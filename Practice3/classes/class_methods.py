# Метод класса
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)

student1 = Student("Ануар", 18)
student1.show_info()