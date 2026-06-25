

#Код для преобразования строки snake case в строку camel case.

import re

text = input("Введите snake_case строку: ")

result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print(result)