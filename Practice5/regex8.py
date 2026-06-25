

#Код чтобы разбить строку на заглавные буквы.
import re

text = input("Введите строку: ")

result = re.findall(r"[A-Z][a-z]*", text)

print(result)