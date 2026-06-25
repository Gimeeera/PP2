import re

#Строка которая совпадает со строкой с нулём или более.
text = input("Введите строку: ")

if re.fullmatch(r"ab*", text):
    print("Подходит")
else:
    print("Не подходит")
