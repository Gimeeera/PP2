# Генератор квадратов чисел до n

def squares(n):
    for i in range(n + 1):
        yield i ** 2


n = int(input())

for num in squares(n):
    print(num)