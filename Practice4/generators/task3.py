# Числа которые делятся на 3 и 4

def divisible_numbers(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())

for num in divisible_numbers(n):
    print(num)