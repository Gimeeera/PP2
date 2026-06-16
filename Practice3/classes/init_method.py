# Конструктор класса
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ануар", 18)
student2 = Student("Али", 19)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)