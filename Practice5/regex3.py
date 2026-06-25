import re

#Код чтобы найти последовательности строчных букв, соединённых с подчёркнутым.
text = input("Введите строку: ")

result = re.findall(r"[a-z]+_[a-z]+", text)

print(result)