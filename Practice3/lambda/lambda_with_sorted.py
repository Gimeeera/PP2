# Сортировка чисел
numbers = [5, 2, 8, 1, 9]
result = sorted(numbers)
print(result)


# Сортировка студентов по баллам
students = [
    ("Ануар", 85),
    ("Али", 70),
    ("Дана", 95)
]

result = sorted(students, key=lambda x: x[1])
print(result)

# Сортировка по возрасту
people = [
    {"name": "Ануар", "age": 18},
    {"name": "Али", "age": 20},
    {"name": "Дана", "age": 17}
]

result = sorted(people, key=lambda x: x["age"])
print(result)