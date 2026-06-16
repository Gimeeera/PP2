# Сумма всех чисел
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4, 5))


# Данные студента
def student(**kwargs):
    print(kwargs)

student(name="Ануар", age=18)


# Вывод данных
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Ануар", city="Алматы")