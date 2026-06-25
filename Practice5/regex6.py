

#Код чтобы заменить все появления пробела, запятой или точки двоеточием.

import re

text = input("Введите строку: ")

result = re.sub(r"[ ,\.]", ":", text)

print(result)