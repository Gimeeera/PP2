

#Код чтобы вставлять пробелы между словами, начинающиеся с заглавных букв.
import re

text = input("Введите строку: ")

result = re.sub(r"([A-Z])", r" \1", text)

print(result.strip())