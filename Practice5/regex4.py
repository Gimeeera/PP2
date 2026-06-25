import re

#Код чтобы найти последовательности одной заглавной буквы, за которой следуют строчные буквы.
text = input("Введите строку: ")

result = re.findall(r"[A-Z][a-z]+", text)

print(result)