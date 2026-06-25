names = ["Ануар", "Али", "Данияр"]

# Нумерация элементов
for index, name in enumerate(names):
    print(index, name)

subjects = ["Math", "Python", "English"]
scores = [90, 85, 95]

# Соединяем списки
for subject, score in zip(subjects, scores):
    print(subject, score)

# Проверка типа
number = "123"

print(type(number))

# Преобразование типов
print(int(number))
print(float(number))