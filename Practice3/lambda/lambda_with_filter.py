# Только четные числа
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


# Числа больше 10
numbers = [5, 10, 15, 20, 25]
result = list(filter(lambda x: x > 10, numbers))
print(result) 