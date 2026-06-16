# Переменная класса
class Student:
    university = "KBTU"

    def __init__(self, name):
        self.name = name

student1 = Student("Ануар")
student2 = Student("Али")

print(student1.university)
print(student1.name)

print(student2.university)
print(student2.name)
