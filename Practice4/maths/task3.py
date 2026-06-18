import math
#Площадб многоугольника

n = int(input("Введите количество сторон: "))
a = int(input("Введите длину стороны: "))
s = (n * a ** 2) / (4 * math.tan(math.pi / n))
print("Площадь многоугольника:", round(s))