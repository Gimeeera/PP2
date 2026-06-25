from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Умножаем каждый элемент на 2
result_map = list(map(lambda x: x * 2, numbers))
print(result_map)

# Оставляем только четные
result_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(result_filter)

# Сумма всех элементов
result_reduce = reduce(lambda x, y: x + y, numbers)
print(result_reduce)